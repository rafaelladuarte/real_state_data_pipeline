(()=>{"use strict";function e(e){const t=Number(e)||9;return Math.round(Math.random()*t)}function t(){var t=function(){for(var e=document.cookie.split("; "),t=0;t<e.length;t++){var o=e[t].split("=");if("GZUID"===o[0])return o[1]}}(),o=null;if(!t)try{t=function(e){const t=window.btoa,o=window.ArrayBuffer;if("function"==typeof t)return t(e);if("function"==typeof o)return o(e).toString("base64");throw new Error("No encode method found")}((Math.random()+"").replace("0.",e())+Date.now()+(Date.now()+"").substring(e(5),e(5))),document.cookie="GZUID="+t+"; SameSite=None; Secure"}catch(e){o=e}return{GZUID:t,ERROR:o}}function o(){window.parent.postMessage(t(),"*")}const n={deleteCookie:function(e){e.cookies.forEach((function(e){const t=e.path?`; path=${e.path}`:"; path=/",o=e.domain?`; domain=${e.domain}`:"",n=e.sameSite?`; SameSite=${e.sameSite}`:"",i=e.secure?"; Secure":"";document.cookie=`${e.name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC${t}${o}${n}${i}`}))},sendGzuid:o,readCookie:function(e){const t=document.cookie.split(";"),o={};t.forEach((function(t){const n=t.split("="),i=n[0].trim(),a=n[1].trim();e.cookies.includes(i)&&(o[i]=a)})),window.parent.postMessage(o,"*")},writeCookie:function(e){e.cookies.forEach((function(e){const t=e.expires?`; expires=${e.expires}`:"",o=e.path?`; path=${e.path}`:"; path=/",n=e.domain?`; domain=${e.domain}`:"",i=e.sameSite?`; SameSite=${e.sameSite}`:"",a=e.secure?"; Secure":"";document.cookie=`${e.name}=${e.value}${t}${o}${n}${i}${a}`}))}};window.addEventListener("message",(function(e){if(!e.data||e.data&&!e.data.type)return console.log(`INFO: no event type specified. The valid types are: ${Object.keys(n)}`);try{n[e.data.type](e.data)}catch(e){console.log("ERROR: ",e)}})),o()})();