(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[802],{80098:function(e,t,n){"use strict";var r,i,a=n(69030),u=n(2265),o=n(99132),s=n(22426),c={out:"out-in",in:"in-out"},l=function(e,t,n){return function(){var r;e.props[t]&&(r=e.props)[t].apply(r,arguments),n()}},f=((r={})[c.out]=function(e){var t=e.current,n=e.changeState;return u.cloneElement(t,{in:!1,onExited:l(t,"onExited",function(){n(o.d0,null)})})},r[c.in]=function(e){var t=e.current,n=e.changeState,r=e.children;return[t,u.cloneElement(r,{in:!0,onEntered:l(r,"onEntered",function(){n(o.d0)})})]},r),d=((i={})[c.out]=function(e){var t=e.children,n=e.changeState;return u.cloneElement(t,{in:!0,onEntered:l(t,"onEntered",function(){n(o.cn,u.cloneElement(t,{in:!0}))})})},i[c.in]=function(e){var t=e.current,n=e.children,r=e.changeState;return[u.cloneElement(t,{in:!1,onExited:l(t,"onExited",function(){r(o.cn,u.cloneElement(n,{in:!0}))})}),u.cloneElement(n,{in:!0})]},i),h=function(e){function t(){for(var t,n=arguments.length,r=Array(n),i=0;i<n;i++)r[i]=arguments[i];return(t=e.call.apply(e,[this].concat(r))||this).state={status:o.cn,current:null},t.appeared=!1,t.changeState=function(e,n){void 0===n&&(n=t.state.current),t.setState({status:e,current:n})},t}(0,a.Z)(t,e);var n=t.prototype;return n.componentDidMount=function(){this.appeared=!0},t.getDerivedStateFromProps=function(e,t){var n,r;return null==e.children?{current:null}:t.status===o.d0&&e.mode===c.in?{status:o.d0}:t.current&&!((n=t.current)===(r=e.children)||u.isValidElement(n)&&u.isValidElement(r)&&null!=n.key&&n.key===r.key)?{status:o.Ix}:{current:u.cloneElement(e.children,{in:!0})}},n.render=function(){var e,t=this.props,n=t.children,r=t.mode,i=this.state,a=i.status,c=i.current,l={children:n,current:c,changeState:this.changeState,status:a};switch(a){case o.d0:e=d[r](l);break;case o.Ix:e=f[r](l);break;case o.cn:e=c}return u.createElement(s.Z.Provider,{value:{isMounting:!this.appeared}},e)},t}(u.Component);h.propTypes={},h.defaultProps={mode:c.out},t.Z=h},13313:function(e,t){"use strict";let n;Object.defineProperty(t,"__esModule",{value:!0}),function(e,t){for(var n in t)Object.defineProperty(e,n,{enumerable:!0,get:t[n]})}(t,{DOMAttributeNames:function(){return r},isEqualNode:function(){return a},default:function(){return u}});let r={acceptCharset:"accept-charset",className:"class",htmlFor:"for",httpEquiv:"http-equiv",noModule:"noModule"};function i(e){let{type:t,props:n}=e,i=document.createElement(t);for(let e in n){if(!n.hasOwnProperty(e)||"children"===e||"dangerouslySetInnerHTML"===e||void 0===n[e])continue;let a=r[e]||e.toLowerCase();"script"===t&&("async"===a||"defer"===a||"noModule"===a)?i[a]=!!n[e]:i.setAttribute(a,n[e])}let{children:a,dangerouslySetInnerHTML:u}=n;return u?i.innerHTML=u.__html||"":a&&(i.textContent="string"==typeof a?a:Array.isArray(a)?a.join(""):""),i}function a(e,t){if(e instanceof HTMLElement&&t instanceof HTMLElement){let n=t.getAttribute("nonce");if(n&&!e.getAttribute("nonce")){let r=t.cloneNode(!0);return r.setAttribute("nonce",""),r.nonce=n,n===e.nonce&&e.isEqualNode(r)}}return e.isEqualNode(t)}function u(){return{mountedInstances:new Set,updateHead:e=>{let t={};e.forEach(e=>{if("link"===e.type&&e.props["data-optimized-fonts"]){if(document.querySelector('style[data-href="'+e.props["data-href"]+'"]'))return;e.props.href=e.props["data-href"],e.props["data-href"]=void 0}let n=t[e.type]||[];n.push(e),t[e.type]=n});let r=t.title?t.title[0]:null,i="";if(r){let{children:e}=r.props;i="string"==typeof e?e:Array.isArray(e)?e.join(""):""}i!==document.title&&(document.title=i),["meta","base","link","style","script"].forEach(e=>{n(e,t[e]||[])})}}}n=(e,t)=>{let n=document.getElementsByTagName("head")[0],r=n.querySelector("meta[name=next-head-count]"),u=Number(r.content),o=[];for(let t=0,n=r.previousElementSibling;t<u;t++,n=(null==n?void 0:n.previousElementSibling)||null){var s;(null==n?void 0:null==(s=n.tagName)?void 0:s.toLowerCase())===e&&o.push(n)}let c=t.map(i).filter(e=>{for(let t=0,n=o.length;t<n;t++)if(a(o[t],e))return o.splice(t,1),!1;return!0});o.forEach(e=>{var t;return null==(t=e.parentNode)?void 0:t.removeChild(e)}),c.forEach(e=>n.insertBefore(e,r)),r.content=(u-o.length+c.length).toString()},("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},85935:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),function(e,t){for(var n in t)Object.defineProperty(e,n,{enumerable:!0,get:t[n]})}(t,{handleClientScriptLoad:function(){return m},initScriptLoader:function(){return y},default:function(){return g}});let r=n(69278),i=n(29325),a=r._(n(54887)),u=i._(n(2265)),o=n(27484),s=n(13313),c=n(52185),l=new Map,f=new Set,d=["onLoad","onReady","dangerouslySetInnerHTML","children","onError","strategy","stylesheets"],h=e=>{if(a.default.preinit){e.forEach(e=>{a.default.preinit(e,{as:"style"})});return}{let t=document.head;e.forEach(e=>{let n=document.createElement("link");n.type="text/css",n.rel="stylesheet",n.href=e,t.appendChild(n)})}},p=e=>{let{src:t,id:n,onLoad:r=()=>{},onReady:i=null,dangerouslySetInnerHTML:a,children:u="",strategy:o="afterInteractive",onError:c,stylesheets:p}=e,m=n||t;if(m&&f.has(m))return;if(l.has(t)){f.add(m),l.get(t).then(r,c);return}let y=()=>{i&&i(),f.add(m)},v=document.createElement("script"),g=new Promise((e,t)=>{v.addEventListener("load",function(t){e(),r&&r.call(this,t),y()}),v.addEventListener("error",function(e){t(e)})}).catch(function(e){c&&c(e)});for(let[n,r]of(a?(v.innerHTML=a.__html||"",y()):u?(v.textContent="string"==typeof u?u:Array.isArray(u)?u.join(""):"",y()):t&&(v.src=t,l.set(t,g)),Object.entries(e))){if(void 0===r||d.includes(n))continue;let e=s.DOMAttributeNames[n]||n.toLowerCase();v.setAttribute(e,r)}"worker"===o&&v.setAttribute("type","text/partytown"),v.setAttribute("data-nscript",o),p&&h(p),document.body.appendChild(v)};function m(e){let{strategy:t="afterInteractive"}=e;"lazyOnload"===t?window.addEventListener("load",()=>{(0,c.requestIdleCallback)(()=>p(e))}):p(e)}function y(e){e.forEach(m),[...document.querySelectorAll('[data-nscript="beforeInteractive"]'),...document.querySelectorAll('[data-nscript="beforePageRender"]')].forEach(e=>{let t=e.id||e.getAttribute("src");f.add(t)})}function v(e){let{id:t,src:n="",onLoad:r=()=>{},onReady:i=null,strategy:s="afterInteractive",onError:l,stylesheets:d,...h}=e,{updateScripts:m,scripts:y,getIsSsr:v,appDir:g,nonce:b}=(0,u.useContext)(o.HeadManagerContext),E=(0,u.useRef)(!1);(0,u.useEffect)(()=>{let e=t||n;E.current||(i&&e&&f.has(e)&&i(),E.current=!0)},[i,t,n]);let C=(0,u.useRef)(!1);if((0,u.useEffect)(()=>{!C.current&&("afterInteractive"===s?p(e):"lazyOnload"===s&&("complete"===document.readyState?(0,c.requestIdleCallback)(()=>p(e)):window.addEventListener("load",()=>{(0,c.requestIdleCallback)(()=>p(e))})),C.current=!0)},[e,s]),("beforeInteractive"===s||"worker"===s)&&(m?(y[s]=(y[s]||[]).concat([{id:t,src:n,onLoad:r,onReady:i,onError:l,...h}]),m(y)):v&&v()?f.add(t||n):v&&!v()&&p(e)),g){if(d&&d.forEach(e=>{a.default.preinit(e,{as:"style"})}),"beforeInteractive"===s)return n?(a.default.preload(n,h.integrity?{as:"script",integrity:h.integrity}:{as:"script"}),u.default.createElement("script",{nonce:b,dangerouslySetInnerHTML:{__html:"(self.__next_s=self.__next_s||[]).push("+JSON.stringify([n])+")"}})):(h.dangerouslySetInnerHTML&&(h.children=h.dangerouslySetInnerHTML.__html,delete h.dangerouslySetInnerHTML),u.default.createElement("script",{nonce:b,dangerouslySetInnerHTML:{__html:"(self.__next_s=self.__next_s||[]).push("+JSON.stringify([0,{...h}])+")"}}));"afterInteractive"===s&&n&&a.default.preload(n,h.integrity?{as:"script",integrity:h.integrity}:{as:"script"})}return null}Object.defineProperty(v,"__nextScript",{value:!0});let g=v;("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},66948:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"useReportWebVitals",{enumerable:!0,get:function(){return a}});let r=n(2265),i=n(91952);function a(e){(0,r.useEffect)(()=>{(0,i.onCLS)(e),(0,i.onFID)(e),(0,i.onLCP)(e),(0,i.onINP)(e),(0,i.onFCP)(e),(0,i.onTTFB)(e)},[e])}("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},251:function(){},79693:function(){},61147:function(e){e.exports={style:{fontFamily:"'__Poppins_79eaae', '__Poppins_Fallback_79eaae'"},className:"__className_79eaae"}},63192:function(e){e.exports={style:{fontFamily:"'__Roboto_06d5da', '__Roboto_Fallback_06d5da'"},className:"__className_06d5da"}},91952:function(e){var t,n,r,i,a,u,o,s,c,l,f,d,h,p,m,y,v,g,b,E,C,_,T,S,O,q,w,A,M,P,I,L,D,Q,x,F,k,N,j,H,R,V,B,Z,K,z;(t={}).d=function(e,n){for(var r in n)t.o(n,r)&&!t.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:n[r]})},t.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},t.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},void 0!==t&&(t.ab="//"),n={},t.r(n),t.d(n,{getCLS:function(){return T},getFCP:function(){return E},getFID:function(){return P},getINP:function(){return V},getLCP:function(){return Z},getTTFB:function(){return z},onCLS:function(){return T},onFCP:function(){return E},onFID:function(){return P},onINP:function(){return V},onLCP:function(){return Z},onTTFB:function(){return z}}),s=-1,c=function(e){addEventListener("pageshow",function(t){t.persisted&&(s=t.timeStamp,e(t))},!0)},l=function(){return window.performance&&performance.getEntriesByType&&performance.getEntriesByType("navigation")[0]},f=function(){var e=l();return e&&e.activationStart||0},d=function(e,t){var n=l(),r="navigate";return s>=0?r="back-forward-cache":n&&(r=document.prerendering||f()>0?"prerender":n.type.replace(/_/g,"-")),{name:e,value:void 0===t?-1:t,rating:"good",delta:0,entries:[],id:"v3-".concat(Date.now(),"-").concat(Math.floor(8999999999999*Math.random())+1e12),navigationType:r}},h=function(e,t,n){try{if(PerformanceObserver.supportedEntryTypes.includes(e)){var r=new PerformanceObserver(function(e){t(e.getEntries())});return r.observe(Object.assign({type:e,buffered:!0},n||{})),r}}catch(e){}},p=function(e,t){var n=function n(r){"pagehide"!==r.type&&"hidden"!==document.visibilityState||(e(r),t&&(removeEventListener("visibilitychange",n,!0),removeEventListener("pagehide",n,!0)))};addEventListener("visibilitychange",n,!0),addEventListener("pagehide",n,!0)},m=function(e,t,n,r){var i,a;return function(u){var o;t.value>=0&&(u||r)&&((a=t.value-(i||0))||void 0===i)&&(i=t.value,t.delta=a,t.rating=(o=t.value)>n[1]?"poor":o>n[0]?"needs-improvement":"good",e(t))}},y=-1,v=function(){return"hidden"!==document.visibilityState||document.prerendering?1/0:0},g=function(){p(function(e){y=e.timeStamp},!0)},b=function(){return y<0&&(y=v(),g(),c(function(){setTimeout(function(){y=v(),g()},0)})),{get firstHiddenTime(){return y}}},E=function(e,t){t=t||{};var n,r=[1800,3e3],i=b(),a=d("FCP"),u=function(e){e.forEach(function(e){"first-contentful-paint"===e.name&&(s&&s.disconnect(),e.startTime<i.firstHiddenTime&&(a.value=e.startTime-f(),a.entries.push(e),n(!0)))})},o=window.performance&&window.performance.getEntriesByName&&window.performance.getEntriesByName("first-contentful-paint")[0],s=o?null:h("paint",u);(o||s)&&(n=m(e,a,r,t.reportAllChanges),o&&u([o]),c(function(i){n=m(e,a=d("FCP"),r,t.reportAllChanges),requestAnimationFrame(function(){requestAnimationFrame(function(){a.value=performance.now()-i.timeStamp,n(!0)})})}))},C=!1,_=-1,T=function(e,t){t=t||{};var n=[.1,.25];C||(E(function(e){_=e.value}),C=!0);var r,i=function(t){_>-1&&e(t)},a=d("CLS",0),u=0,o=[],s=function(e){e.forEach(function(e){if(!e.hadRecentInput){var t=o[0],n=o[o.length-1];u&&e.startTime-n.startTime<1e3&&e.startTime-t.startTime<5e3?(u+=e.value,o.push(e)):(u=e.value,o=[e]),u>a.value&&(a.value=u,a.entries=o,r())}})},l=h("layout-shift",s);l&&(r=m(i,a,n,t.reportAllChanges),p(function(){s(l.takeRecords()),r(!0)}),c(function(){u=0,_=-1,r=m(i,a=d("CLS",0),n,t.reportAllChanges)}))},S={passive:!0,capture:!0},O=new Date,q=function(e,t){r||(r=t,i=e,a=new Date,M(removeEventListener),w())},w=function(){if(i>=0&&i<a-O){var e={entryType:"first-input",name:r.type,target:r.target,cancelable:r.cancelable,startTime:r.timeStamp,processingStart:r.timeStamp+i};u.forEach(function(t){t(e)}),u=[]}},A=function(e){if(e.cancelable){var t,n,r,i=(e.timeStamp>1e12?new Date:performance.now())-e.timeStamp;"pointerdown"==e.type?(t=function(){q(i,e),r()},n=function(){r()},r=function(){removeEventListener("pointerup",t,S),removeEventListener("pointercancel",n,S)},addEventListener("pointerup",t,S),addEventListener("pointercancel",n,S)):q(i,e)}},M=function(e){["mousedown","keydown","touchstart","pointerdown"].forEach(function(t){return e(t,A,S)})},P=function(e,t){t=t||{};var n,a=[100,300],o=b(),s=d("FID"),l=function(e){e.startTime<o.firstHiddenTime&&(s.value=e.processingStart-e.startTime,s.entries.push(e),n(!0))},f=function(e){e.forEach(l)},y=h("first-input",f);n=m(e,s,a,t.reportAllChanges),y&&p(function(){f(y.takeRecords()),y.disconnect()},!0),y&&c(function(){n=m(e,s=d("FID"),a,t.reportAllChanges),u=[],i=-1,r=null,M(addEventListener),u.push(l),w()})},I=0,L=1/0,D=0,Q=function(e){e.forEach(function(e){e.interactionId&&(L=Math.min(L,e.interactionId),I=(D=Math.max(D,e.interactionId))?(D-L)/7+1:0)})},x=function(){return o?I:performance.interactionCount||0},F=function(){"interactionCount"in performance||o||(o=h("event",Q,{type:"event",buffered:!0,durationThreshold:0}))},k=0,N=function(){return x()-k},j=[],H={},R=function(e){var t=j[j.length-1],n=H[e.interactionId];if(n||j.length<10||e.duration>t.latency){if(n)n.entries.push(e),n.latency=Math.max(n.latency,e.duration);else{var r={id:e.interactionId,latency:e.duration,entries:[e]};H[r.id]=r,j.push(r)}j.sort(function(e,t){return t.latency-e.latency}),j.splice(10).forEach(function(e){delete H[e.id]})}},V=function(e,t){t=t||{};var n=[200,500];F();var r,i=d("INP"),a=function(e){e.forEach(function(e){e.interactionId&&R(e),"first-input"!==e.entryType||j.some(function(t){return t.entries.some(function(t){return e.duration===t.duration&&e.startTime===t.startTime})})||R(e)});var t,n=(t=Math.min(j.length-1,Math.floor(N()/50)),j[t]);n&&n.latency!==i.value&&(i.value=n.latency,i.entries=n.entries,r())},u=h("event",a,{durationThreshold:t.durationThreshold||40});r=m(e,i,n,t.reportAllChanges),u&&(u.observe({type:"first-input",buffered:!0}),p(function(){a(u.takeRecords()),i.value<0&&N()>0&&(i.value=0,i.entries=[]),r(!0)}),c(function(){j=[],k=x(),r=m(e,i=d("INP"),n,t.reportAllChanges)}))},B={},Z=function(e,t){t=t||{};var n,r=[2500,4e3],i=b(),a=d("LCP"),u=function(e){var t=e[e.length-1];if(t){var r=t.startTime-f();r<i.firstHiddenTime&&(a.value=r,a.entries=[t],n())}},o=h("largest-contentful-paint",u);if(o){n=m(e,a,r,t.reportAllChanges);var s=function(){B[a.id]||(u(o.takeRecords()),o.disconnect(),B[a.id]=!0,n(!0))};["keydown","click"].forEach(function(e){addEventListener(e,s,{once:!0,capture:!0})}),p(s,!0),c(function(i){n=m(e,a=d("LCP"),r,t.reportAllChanges),requestAnimationFrame(function(){requestAnimationFrame(function(){a.value=performance.now()-i.timeStamp,B[a.id]=!0,n(!0)})})})}},K=function e(t){document.prerendering?addEventListener("prerenderingchange",function(){return e(t)},!0):"complete"!==document.readyState?addEventListener("load",function(){return e(t)},!0):setTimeout(t,0)},z=function(e,t){t=t||{};var n=[800,1800],r=d("TTFB"),i=m(e,r,n,t.reportAllChanges);K(function(){var a=l();if(a){if(r.value=Math.max(a.responseStart-f(),0),r.value<0||r.value>performance.now())return;r.entries=[a],i(!0),c(function(){(i=m(e,r=d("TTFB",0),n,t.reportAllChanges))(!0)})}})},e.exports=n},95509:function(e,t,n){e.exports=n(66948)},28062:function(e,t,n){"use strict";n.d(t,{S:function(){return p}});var r=n(72348),i=n(28631),a=n(60975),u=n(47133),o=class extends u.l{constructor(e={}){super(),this.config=e,this.#e=new Map}#e;build(e,t,n){let a=t.queryKey,u=t.queryHash??(0,r.Rm)(a,t),o=this.get(u);return o||(o=new i.A({cache:this,queryKey:a,queryHash:u,options:e.defaultQueryOptions(t),state:n,defaultOptions:e.getQueryDefaults(a)}),this.add(o)),o}add(e){this.#e.has(e.queryHash)||(this.#e.set(e.queryHash,e),this.notify({type:"added",query:e}))}remove(e){let t=this.#e.get(e.queryHash);t&&(e.destroy(),t===e&&this.#e.delete(e.queryHash),this.notify({type:"removed",query:e}))}clear(){a.V.batch(()=>{this.getAll().forEach(e=>{this.remove(e)})})}get(e){return this.#e.get(e)}getAll(){return[...this.#e.values()]}find(e){let t={exact:!0,...e};return this.getAll().find(e=>(0,r._x)(t,e))}findAll(e={}){let t=this.getAll();return Object.keys(e).length>0?t.filter(t=>(0,r._x)(e,t)):t}notify(e){a.V.batch(()=>{this.listeners.forEach(t=>{t(e)})})}onFocus(){a.V.batch(()=>{this.getAll().forEach(e=>{e.onFocus()})})}onOnline(){a.V.batch(()=>{this.getAll().forEach(e=>{e.onOnline()})})}},s=n(75115),c=class extends u.l{constructor(e={}){super(),this.config=e,this.#t=new Map,this.#n=Date.now()}#t;#n;build(e,t,n){let r=new s.m({mutationCache:this,mutationId:++this.#n,options:e.defaultMutationOptions(t),state:n});return this.add(r),r}add(e){let t=l(e),n=this.#t.get(t)??[];n.push(e),this.#t.set(t,n),this.notify({type:"added",mutation:e})}remove(e){let t=l(e);if(this.#t.has(t)){let n=this.#t.get(t)?.filter(t=>t!==e);n&&(0===n.length?this.#t.delete(t):this.#t.set(t,n))}this.notify({type:"removed",mutation:e})}canRun(e){let t=this.#t.get(l(e))?.find(e=>"pending"===e.state.status);return!t||t===e}runNext(e){let t=this.#t.get(l(e))?.find(t=>t!==e&&t.state.isPaused);return t?.continue()??Promise.resolve()}clear(){a.V.batch(()=>{this.getAll().forEach(e=>{this.remove(e)})})}getAll(){return[...this.#t.values()].flat()}find(e){let t={exact:!0,...e};return this.getAll().find(e=>(0,r.X7)(t,e))}findAll(e={}){return this.getAll().filter(t=>(0,r.X7)(e,t))}notify(e){a.V.batch(()=>{this.listeners.forEach(t=>{t(e)})})}resumePausedMutations(){let e=this.getAll().filter(e=>e.state.isPaused);return a.V.batch(()=>Promise.all(e.map(e=>e.continue().catch(r.ZT))))}};function l(e){return e.options.scope?.id??String(e.mutationId)}var f=n(16418),d=n(81041),h=n(64563),p=class{#r;#i;#a;#u;#o;#s;#c;#l;constructor(e={}){this.#r=e.queryCache||new o,this.#i=e.mutationCache||new c,this.#a=e.defaultOptions||{},this.#u=new Map,this.#o=new Map,this.#s=0}mount(){this.#s++,1===this.#s&&(this.#c=f.j.subscribe(async e=>{e&&(await this.resumePausedMutations(),this.#r.onFocus())}),this.#l=d.N.subscribe(async e=>{e&&(await this.resumePausedMutations(),this.#r.onOnline())}))}unmount(){this.#s--,0===this.#s&&(this.#c?.(),this.#c=void 0,this.#l?.(),this.#l=void 0)}isFetching(e){return this.#r.findAll({...e,fetchStatus:"fetching"}).length}isMutating(e){return this.#i.findAll({...e,status:"pending"}).length}getQueryData(e){let t=this.defaultQueryOptions({queryKey:e});return this.#r.get(t.queryHash)?.state.data}ensureQueryData(e){let t=this.getQueryData(e.queryKey);if(void 0===t)return this.fetchQuery(e);{let n=this.defaultQueryOptions(e),i=this.#r.build(this,n);return e.revalidateIfStale&&i.isStaleByTime((0,r.KC)(n.staleTime,i))&&this.prefetchQuery(n),Promise.resolve(t)}}getQueriesData(e){return this.#r.findAll(e).map(({queryKey:e,state:t})=>[e,t.data])}setQueryData(e,t,n){let i=this.defaultQueryOptions({queryKey:e}),a=this.#r.get(i.queryHash),u=a?.state.data,o=(0,r.SE)(t,u);if(void 0!==o)return this.#r.build(this,i).setData(o,{...n,manual:!0})}setQueriesData(e,t,n){return a.V.batch(()=>this.#r.findAll(e).map(({queryKey:e})=>[e,this.setQueryData(e,t,n)]))}getQueryState(e){let t=this.defaultQueryOptions({queryKey:e});return this.#r.get(t.queryHash)?.state}removeQueries(e){let t=this.#r;a.V.batch(()=>{t.findAll(e).forEach(e=>{t.remove(e)})})}resetQueries(e,t){let n=this.#r,r={type:"active",...e};return a.V.batch(()=>(n.findAll(e).forEach(e=>{e.reset()}),this.refetchQueries(r,t)))}cancelQueries(e={},t={}){let n={revert:!0,...t};return Promise.all(a.V.batch(()=>this.#r.findAll(e).map(e=>e.cancel(n)))).then(r.ZT).catch(r.ZT)}invalidateQueries(e={},t={}){return a.V.batch(()=>{if(this.#r.findAll(e).forEach(e=>{e.invalidate()}),"none"===e.refetchType)return Promise.resolve();let n={...e,type:e.refetchType??e.type??"active"};return this.refetchQueries(n,t)})}refetchQueries(e={},t){let n={...t,cancelRefetch:t?.cancelRefetch??!0};return Promise.all(a.V.batch(()=>this.#r.findAll(e).filter(e=>!e.isDisabled()).map(e=>{let t=e.fetch(void 0,n);return n.throwOnError||(t=t.catch(r.ZT)),"paused"===e.state.fetchStatus?Promise.resolve():t}))).then(r.ZT)}fetchQuery(e){let t=this.defaultQueryOptions(e);void 0===t.retry&&(t.retry=!1);let n=this.#r.build(this,t);return n.isStaleByTime((0,r.KC)(t.staleTime,n))?n.fetch(t):Promise.resolve(n.state.data)}prefetchQuery(e){return this.fetchQuery(e).then(r.ZT).catch(r.ZT)}fetchInfiniteQuery(e){return e.behavior=(0,h.Gm)(e.pages),this.fetchQuery(e)}prefetchInfiniteQuery(e){return this.fetchInfiniteQuery(e).then(r.ZT).catch(r.ZT)}resumePausedMutations(){return d.N.isOnline()?this.#i.resumePausedMutations():Promise.resolve()}getQueryCache(){return this.#r}getMutationCache(){return this.#i}getDefaultOptions(){return this.#a}setDefaultOptions(e){this.#a=e}setQueryDefaults(e,t){this.#u.set((0,r.Ym)(e),{queryKey:e,defaultOptions:t})}getQueryDefaults(e){let t=[...this.#u.values()],n={};return t.forEach(t=>{(0,r.to)(e,t.queryKey)&&(n={...n,...t.defaultOptions})}),n}setMutationDefaults(e,t){this.#o.set((0,r.Ym)(e),{mutationKey:e,defaultOptions:t})}getMutationDefaults(e){let t=[...this.#o.values()],n={};return t.forEach(t=>{(0,r.to)(e,t.mutationKey)&&(n={...n,...t.defaultOptions})}),n}defaultQueryOptions(e){if(e._defaulted)return e;let t={...this.#a.queries,...this.getQueryDefaults(e.queryKey),...e,_defaulted:!0};return t.queryHash||(t.queryHash=(0,r.Rm)(t.queryKey,t)),void 0===t.refetchOnReconnect&&(t.refetchOnReconnect="always"!==t.networkMode),void 0===t.throwOnError&&(t.throwOnError=!!t.suspense),!t.networkMode&&t.persister&&(t.networkMode="offlineFirst"),!0!==t.enabled&&t.queryFn===r.CN&&(t.enabled=!1),t}defaultMutationOptions(e){return e?._defaulted?e:{...this.#a.mutations,...e?.mutationKey&&this.getMutationDefaults(e.mutationKey),...e,_defaulted:!0}}clear(){this.#r.clear(),this.#i.clear()}}},77034:function(e,t,n){"use strict";n.d(t,{t:function(){return r}});var r=function(){return null}}}]);