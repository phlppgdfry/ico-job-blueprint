import {useEffect,useState} from 'react';
import {initialState,loadState,validateState,STORAGE_KEY} from './model.mjs';
export function useProgress(){
 const [state,setState]=useState(()=>loadState(localStorage));
 const [storageError,setStorageError]=useState('');
 useEffect(()=>{document.documentElement.dataset.theme=state.theme;try{localStorage.setItem(STORAGE_KEY,JSON.stringify(state));setStorageError('');}catch{setStorageError('Opslaan in deze browser is geblokkeerd of vol. Exporteer je voortgang om verlies te voorkomen.');}},[state]);
 const put=(field,key,value)=>setState(s=>({...s,[field]:{...s[field],[key]:value}}));
 const toggle=(field,key)=>setState(s=>({...s,[field]:{...s[field],[key]:!s[field][key]}}));
 const theme=()=>setState(s=>({...s,theme:s.theme==='light'?'dark':'light'}));
 const importState=raw=>setState(validateState(raw));
 const reset=()=>setState(initialState());
 return {state,put,toggle,theme,importState,reset,storageError};
}
