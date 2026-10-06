export const STORAGE_KEY='ico-role-os:v1';
export const initialState=()=>({schema:1,theme:'light',done:{},checks:{},skillLevels:{},proof:{},requirementProof:{},scenarioAnswers:{},scenarioRubrics:{},interviewAnswers:{},interviewRubrics:{},roadmap:{},notes:{}});
export function validateState(raw){
  if(!raw||raw.schema!==1||typeof raw!=='object'||Array.isArray(raw))throw new Error('Ongeldig exportformaat: verwacht ROLE / OS versie 1.');
  const out=initialState();
  for(const key of Object.keys(out)){
    if(key==='schema')continue;
    if(key==='theme'){out.theme=raw.theme==='dark'?'dark':'light';continue;}
    const value=raw[key];
    if(value!==undefined){
      if(!value||typeof value!=='object'||Array.isArray(value))throw new Error(`Ongeldig veld: ${key}`);
      const booleans=['done','checks','scenarioRubrics','interviewRubrics','roadmap'].includes(key);
      for(const [entry,v] of Object.entries(value)){
        if(typeof v!==(booleans?'boolean':'string'))throw new Error(`Ongeldige waarde in ${key}.`);
        if(key==='done'&&(!/^\d+$/.test(entry)||Number(entry)<1||Number(entry)>30))throw new Error('Ongeldig hoofdstuknummer.');
        if(key==='skillLevels'&&!['Niet beoordeeld','Theorie kennen','Begrijpen','Met hulp uitvoeren','Zelfstandig uitvoeren','Expert'].includes(v))throw new Error('Onbekend skillniveau.');
      }
      out[key]=value;
    }
  }
  return out;
}
export function loadState(storage){try{const raw=storage.getItem(STORAGE_KEY);return raw?validateState(JSON.parse(raw)):initialState();}catch{return initialState();}}
export function chapterProgress(state,total=30){return Math.round(Object.values(state.done).filter(x=>x===true).length/total*100);}
export function normalize(value){return String(value).normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLocaleLowerCase('nl');}
export function searchContent(data,query){
 const needle=normalize(query.trim());if(!needle)return [];
 const records=[...data.chapters.flatMap(x=>splitSections(x.body).map((section,i)=>({kind:'Hoofdstuk',title:`${String(x.id).padStart(2,'0')} · ${x.title} / ${section.title}`,text:section.body,to:`chapter/${x.id}/${i}`}))),...data.scenarios.map(x=>({kind:'Scenario',title:x.title,text:Object.values(x).flat().join(' '),to:`scenarios/${x.id}`})),...data.interviews.map(x=>({kind:'Interview',title:x.question,text:Object.values(x).flat().join(' '),to:`interview/${x.id}`})),{kind:'Research',title:'Bronnen & betrouwbaarheid',text:data.sources,to:'sources'}];
 return records.filter(x=>normalize(x.title+' '+x.text).includes(needle)).map(x=>{
  const idx=normalize(x.text).indexOf(needle);return {...x,excerpt:x.text.slice(Math.max(0,idx-65),Math.max(0,idx-65)+180).replace(/[#*|\n]/g,' ')};
 });
}
export function splitSections(body){
 const parts=body.split(/^## /m);return parts.map((text,i)=>i===0?{title:'Leeswijzer',body:text}:{title:text.slice(0,text.indexOf('\n')),body:text.slice(text.indexOf('\n')+1)}).filter(x=>x.body.trim());
}
