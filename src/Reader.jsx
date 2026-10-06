import {useEffect,useState} from 'react';
import Markdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import {CheckCircle2,ChevronLeft,ChevronRight,Printer} from 'lucide-react';
import {splitSections} from './model.mjs';

function taskPlugin(prefix){return ()=>tree=>{let i=0;const walk=node=>{if(node.tagName==='input'&&node.properties?.type==='checkbox')node.properties['data-task-key']=`${prefix}/${i++}`;node.children?.forEach(walk);};walk(tree);};}
export function RichText({body,prefix='text',store}){
 return <div className="prose"><Markdown remarkPlugins={[remarkGfm]} rehypePlugins={[taskPlugin(prefix)]} components={{
   a:({node,...props})=><a {...props} target={props.href?.startsWith('http')?'_blank':undefined} rel="noreferrer"/>,
   h1:({node,...props})=><h2 {...props}/>,
   table:({node,...props})=><div className="table-scroll"><table {...props}/></div>,
   input:({node,checked,disabled,...props})=>{const key=props['data-task-key'];return <input {...props} aria-label="Checklistpunt" checked={store?!!store.state.checks[key]:!!checked} disabled={!store} onChange={()=>store?.toggle('checks',key)}/>;}
 }} >{body}</Markdown></div>;
}
export function ChapterReader({chapter,sectionId,store,navigate}){
 const sections=splitSections(chapter.body);
 const [allOpen,setAllOpen]=useState(true);
 useEffect(()=>{if(sectionId!==undefined){const target=document.getElementById(`section-${sectionId}`);if(target){target.open=true;target.scrollIntoView({block:'start'});}}},[sectionId,chapter.id]);
 return <>
 <div className="page-heading"><div><p className="context">Hoofdstuk {String(chapter.id).padStart(2,'0')} / 30</p><h1>{chapter.title}</h1></div><button className="secondary no-print" onClick={()=>window.print()}><Printer size={16}/> Print hoofdstuk</button></div>
 <div className="reader-tools no-print"><label className="check-label"><input type="checkbox" checked={!!store.state.done[chapter.id]} onChange={()=>store.toggle('done',chapter.id)}/><span>Bestudeerd — voortgang, geen bekwaamheidsscore</span></label><button className="text-button" onClick={()=>setAllOpen(x=>!x)}>{allOpen?'Alles inklappen':'Alles uitklappen'}</button></div>
 <article className="reader" key={`${chapter.id}/${allOpen}`}>
 {sections.map((section,i)=><details id={`section-${i}`} key={i} open={allOpen||i===0}><summary>{section.title}</summary><RichText body={section.body} prefix={`chapter/${chapter.id}/${i}`} store={store}/></details>)}
 </article>
 <section className="notes no-print"><label htmlFor="chapter-notes">Mijn notities en open vragen</label><textarea id="chapter-notes" value={store.state.notes[chapter.id]||''} onChange={e=>store.put('notes',chapter.id,e.target.value)} placeholder="Wat kan ik uitleggen? Wat wil ik nog oefenen of aan ICO vragen?"/></section>
 <div className="bottom-nav no-print"><button disabled={chapter.id===1} className="secondary" onClick={()=>navigate(`chapter/${chapter.id-1}`)}><ChevronLeft size={16}/> Vorig hoofdstuk</button><button className="primary" disabled={chapter.id===30} onClick={()=>navigate(`chapter/${chapter.id+1}`)}>Volgend hoofdstuk <ChevronRight size={16}/></button></div>
 </>;
}
export function ChapterList({chapters,store,navigate,title='Hoofdstukken'}){
 return <section className="chapter-list"><h2>{title}</h2><div className="chapter-rows">{chapters.map(c=><div className="chapter-row" key={c.id}><span className="chapter-number">{String(c.id).padStart(2,'0')}</span><button className="chapter-link" onClick={()=>navigate(`chapter/${c.id}`)}><strong>{c.title}</strong><span>{c.summary}</span></button><label className="completion"><input type="checkbox" aria-label={`Hoofdstuk ${c.id} bestudeerd`} checked={!!store.state.done[c.id]} onChange={()=>store.toggle('done',c.id)}/><CheckCircle2 size={23}/></label><button className="icon-button" aria-label={`Open ${c.title}`} onClick={()=>navigate(`chapter/${c.id}`)}><ChevronRight size={20}/></button></div>)}</div></section>;
}
