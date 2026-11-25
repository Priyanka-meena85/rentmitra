const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

// Parse all IDs and build a mock DOM with proxy
const idMatches = html.match(/id=["']([^"']+)["']/g) || [];
const ids = new Set(idMatches.map(m => m.replace(/id=["']/, '').replace(/["']$/, '')));

console.log('Total mock IDs:', ids.size);

// Minimal DOM Mock
const elements = {};
function getOrCreateElem(id) {
  if (!elements[id]) {
    elements[id] = {
      id: id,
      classList: {
        classes: new Set(),
        add(...c) { c.forEach(x => this.classes.add(x)); },
        remove(...c) { c.forEach(x => this.classes.delete(x)); },
        contains(c) { return this.classes.has(c); },
        toggle(c) { if (this.classes.has(c)) this.classes.delete(c); else this.classes.add(c); }
      },
      style: {},
      innerHTML: '',
      innerText: '',
      value: '',
      href: '',
      src: '',
      options: [{ value: 'Test', getAttribute: () => 'Test' }],
      selectedIndex: 0,
      checked: false,
      querySelector: () => ({ classList: { contains: () => false, remove() {}, add() {} } }),
      querySelectorAll: () => [],
      getContext: () => ({
        beginPath() {}, moveTo() {}, lineTo() {}, stroke() {},
        strokeStyle: '', lineWidth: 1, lineCap: ''
      }),
      getBoundingClientRect: () => ({ left: 0, top: 0, width: 100, height: 100 }),
      appendChild() {},
      remove() {}
    };
  }
  return elements[id];
}

global.window = {
  location: { protocol: 'http:' },
  scrollTo() {},
  addEventListener() {},
  event: null
};

global.document = {
  readyState: 'complete',
  getElementById(id) {
    if (!ids.has(id)) {
      console.warn('WARNING: document.getElementById called for NON-EXISTENT ID:', id);
    }
    return getOrCreateElem(id);
  },
  querySelector(sel) {
    return getOrCreateElem('mock-sel');
  },
  querySelectorAll(sel) {
    return [getOrCreateElem('mock-sel-1'), getOrCreateElem('mock-sel-2')];
  },
  createElement(tag) {
    return getOrCreateElem('mock-new-' + tag);
  },
  addEventListener() {},
  body: { style: {} }
};

global.localStorage = {
  store: {},
  getItem(k) { return this.store[k] || null; },
  setItem(k, v) { this.store[k] = v; },
  removeItem(k) { delete this.store[k]; }
};

global.fetch = async () => ({
  ok: true,
  json: async () => ([])
});

// Run main_debug.js
try {
  console.log('--- Executing main_debug.js ---');
  require('./main_debug.js');
  console.log('Execution finished without crashing!');
} catch (err) {
  console.error('RUNTIME ERROR in main_debug.js:', err);
}
