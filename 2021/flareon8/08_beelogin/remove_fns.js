//cite: https://github.com/abdul-manaan/JS_Analysis/blob/fcfa841e3bc6b9c08f82d8652e8e6c1782a6e7a8/Trimmer/trimmer.js
const fs = require('fs')
var esprima = require('esprima')
var escodegen = require('escodegen')
const ESPRIMA_PARSE_SETTINGS = {
    sourceType: 'script',
    loc: true,
    range: true,
    //comment: true,
    //tokens: true
}
//Reading a File Asynchronously
const readFile = f => new Promise((resolve, reject) =>
    fs.readFile(f, 'utf-8', (e, d) => e ? reject(e) : resolve(d)))

//Writing A file
const writeFile = (f, data) => new Promise((resolve, reject) =>
    fs.writeFile(f, data, (e) => e ? reject(e) : resolve("Done")))


var source = fs.readFileSync('beelogin.js', 'utf8');

var parsed = esprima.parse(source, ESPRIMA_PARSE_SETTINGS);
/* Script {
  type: 'Program',
  body: [
    FunctionDeclaration {
      type: 'FunctionDeclaration',
      id: [Identifier],
      params: [Array],
      body: [BlockStatement],
      generator: false,
      expression: false,
      async: false
    }
  ],
  sourceType: 'script'
} */
//console.log(JSON.stringify(parsed, null, 2));

// parsed.body[0];
/*
FunctionDeclaration {
  type: 'FunctionDeclaration',
  id: Identifier { type: 'Identifier', name: 'Add' },
  params: [ Identifier { type: 'Identifier', name: 'submit_group' } ],
  body: BlockStatement {
    type: 'BlockStatement',
    body: [
      [FunctionDeclaration], [EmptyStatement],      [FunctionDeclaration],
      [EmptyStatement],      [FunctionDeclaration], [EmptyStatement],
      [FunctionDeclaration], [EmptyStatement],      [FunctionDeclaration],
      [EmptyStatement],      [FunctionDeclaration], [EmptyStatement],
      [FunctionDeclaration], [EmptyStatement],      [FunctionDeclaration],
      [EmptyStatement],      [FunctionDeclaration], [EmptyStatement],
      [FunctionDeclaration], [EmptyStatement],      [FunctionDeclaration],
      [EmptyStatement],      [FunctionDeclaration], [EmptyStatement],
      [FunctionDeclaration], [EmptyStatement],      [ExpressionStatement],
      [FunctionDeclaration], [EmptyStatement],      [FunctionDeclaration],
      [EmptyStatement],      [FunctionDeclaration], [EmptyStatement],
      [FunctionDeclaration], [EmptyStatement],      [FunctionDeclaration],
      [EmptyStatement],      [FunctionDeclaration], [EmptyStatement],
      [FunctionDeclaration], [EmptyStatement],      [FunctionDeclaration],
      [EmptyStatement],      [FunctionDeclaration], [EmptyStatement],
      [FunctionDeclaration], [EmptyStatement],      [FunctionDeclaration],
      [EmptyStatement],      [FunctionDeclaration], [EmptyStatement],
      [FunctionDeclaration], [EmptyStatement],      [FunctionDeclaration],
      [EmptyStatement],      [FunctionDeclaration], [EmptyStatement],
      [FunctionDeclaration], [EmptyStatement],      [FunctionDeclaration],
      [EmptyStatement],      [FunctionDeclaration], [EmptyStatement],
      [IfStatement],         [FunctionDeclaration], [EmptyStatement],
      [FunctionDeclaration], [EmptyStatement],      [FunctionDeclaration],
      [EmptyStatement],      [FunctionDeclaration], [EmptyStatement],
      [FunctionDeclaration], [EmptyStatement],      [FunctionDeclaration],
      [EmptyStatement],      [FunctionDeclaration], [EmptyStatement],
      [FunctionDeclaration], [EmptyStatement],      [FunctionDeclaration],
      [EmptyStatement],      [FunctionDeclaration], [EmptyStatement],
      [FunctionDeclaration], [EmptyStatement],      [FunctionDeclaration],
      [EmptyStatement],      [FunctionDeclaration], [EmptyStatement],
      [FunctionDeclaration], [EmptyStatement],      [ExpressionStatement],
      [FunctionDeclaration], [EmptyStatement],      [FunctionDeclaration],
      [EmptyStatement],      [FunctionDeclaration], [EmptyStatement],
      [FunctionDeclaration],
      ... 5403 more items
    ]
  },
  generator: false,
  expression: false,
  async: false
} */


function removeFns(source) {
    const entries = [];
    esprima.parseScript(source, {}, function (node, meta) {
        if (isConsoleCall(node)) {
            entries.push({
                start: meta.start.offset,
                end: meta.end.offset
            });
        }
    });
    entries.sort((a, b) => { return b.end - a.end }).forEach(n => {
        source = source.slice(0, n.start)  + source.slice(n.end);
    });
    return source;
}

add_fn_body = parsed.body[0].body.body;
// const entries = [];
// for (i = 0; i < add_fn_body.length; i++) {
//  if (add_fn_body[i].type == 'FunctionDeclaration') { // ExpressionStatement
//         entries.push({
//             start: add_fn_body[i].range[0],
//             end  : add_fn_body[i].range[1]
//         });
// 	}
// }
// entries.sort((a, b) => { return b.end - a.end }).forEach(n => {
//     source = source.slice(0, n.start) + source.slice(n.end+1); // +1 for ';' char.
// });
// console.log(source);

var fns = {};
const entries = [];
var new_source = ''
for (i = 0; i < add_fn_body.length; i++) {
  if (add_fn_body[i].type == 'FunctionDeclaration' && !(add_fn_body[i].id.name in fns)) { // ExpressionStatement
    fns[add_fn_body[i].id.name] = true
    entries.push({
      start: add_fn_body[i].range[0],
      end  : add_fn_body[i].range[1]
    });
  }
}
entries.sort((a, b) => { return a.end - b.end }).forEach(n => {
    new_source += source.slice(n.start, n.end + 1) + '\n'; // +1 for ';' char.
});

console.log(new_source);



// const main = async () => {
//     const args = process.argv;
//     if (args.length < 2) {
//         console.log("Error: node solve.js jsFile")
//     }
//     let source = '';
//     source = await readFile(args[2]);
//     await writeFile(args[2].split('.')[0] + "updated.js", removeFns(source));
//     console.log("Done!");
// }
// main();
