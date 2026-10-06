import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {initialState,validateState,loadState,chapterProgress,searchContent,splitSections,STORAGE_KEY} from '../src/model.mjs';
const data=JSON.parse(fs.readFileSync(new URL('../src/content.json',import.meta.url)));
test('Scope: 30 chapters, all requirement IDs, sufficient cases/questions and complete technology records',()=>{
 assert.deepEqual(data.chapters.map(x=>x.id),Array.from({length:30},(_,i)=>i+1));
 assert.equal(data.requirements.length,35);assert.equal(data.scenarios.length,25);assert.equal(data.interviews.length,56);assert.equal(data.projects.length,3);
 for(const tech of data.tech)for(const key of ['definition','use','why','where','mechanism','can','notneeded','problems','diagnosis','terms','question','answer','exercise','case','hours','level'])assert.ok(tech[key]?.length>15,`${tech.name} / ${key}`);
 for(const cat of ['HR','Motivatie','Techniek','Scenario','Troubleshooting','Business','Gedrag','Ervaring'])assert.equal(data.interviews.filter(x=>x.category===cat).length,7);
 for(const r of data.requirements)assert.ok(data.chapters.find(x=>x.id===2).body.includes(r.id));
});
test('Import preserves real learning data; rejects broken schema/values instead of crashing UI',()=>{
 const saved=initialState();saved.done['6']=true;saved.scenarioAnswers['1']='Mijn test';saved.skillLevels.SQL='Zelfstandig uitvoeren';
 assert.deepEqual(validateState(JSON.parse(JSON.stringify(saved))),saved);assert.equal(chapterProgress(saved),3);
 assert.throws(()=>validateState({schema:2}));assert.throws(()=>validateState({...saved,done:{31:true}}));assert.throws(()=>validateState({...saved,done:{1:'true'}}));assert.throws(()=>validateState({...saved,proof:{SQL:{fake:1}}}));assert.throws(()=>validateState({...saved,skillLevels:{SQL:'superhero'}}));
});
test('Corrupt or unavailable storage falls back safely; valid storage round-trips',()=>{
 assert.deepEqual(loadState({getItem:()=>'{broken'}),initialState());assert.deepEqual(loadState({getItem:()=>{throw Error('blocked')}}),initialState());
 const saved=initialState();saved.checks['chapter/11/1/0']=true;
 assert.deepEqual(loadState({getItem:key=>key===STORAGE_KEY?JSON.stringify(saved):null}),saved);
});
test('Search matches real deep content and opens valid chapter sections or exercises',()=>{
 assert.equal(searchContent(data,'').length,0);assert.equal(searchContent(data,'zzzxxyynotfound').length,0);
 const hits=searchContent(data,'reconciliatie');assert.ok(hits.length>10);assert.ok(hits.some(x=>x.kind==='Scenario'));assert.ok(hits.some(x=>x.kind==='Interview'));
 for(const hit of searchContent(data,'Oracle')){if(hit.to.startsWith('chapter/')){const [,id,index]=hit.to.split('/');assert.ok(splitSections(data.chapters.find(x=>x.id===Number(id)).body)[Number(index)]);}}
});
