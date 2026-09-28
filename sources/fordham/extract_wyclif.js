const fs=require('fs');
const s=fs.readFileSync('main.js','utf8');
const out={}; let i=0; const tag="JSON.parse('";
while((i=s.indexOf(tag,i))!==-1){ let j=i+tag.length, k=j;
 while(true){ if(s[k]==='\\'){k+=2;continue} if(s[k]==="'")break; k++; }
 try{ const arr=JSON.parse(eval("'"+s.slice(j,k)+"'"));
   if(Array.isArray(arr)&&arr[0]&&arr[0].model)(out[arr[0].model]=out[arr[0].model]||[]).push(...arr);}catch(e){}
 i=k; }
for(const k in out) console.log(k,out[k].length);
fs.writeFileSync('data.json',JSON.stringify(out));
