CodeMirror.modeURL = '../../static/assets/codemirror/mode/%N/%N.js';
var code = $(".codemirror-textarea")[0];
var syntax_extension = $(document.getElementById("syntax")).find('option:selected').text();
var editor = CodeMirror.fromTextArea(code, {
    lineNumbers: true,
    matchBrackets: true,
    theme: "blackboard",
    styleActiveLine: true,
    mode: "text",
    extraKeys: {
        "Alt-F": "findPersistent",
        "F11": function(cm) {
            cm.setOption("fullScreen", !cm.getOption("fullScreen"));
        },
        "Esc": function(cm) {
            if (cm.getOption("fullScreen")) cm.setOption("fullScreen", false);
        },
    },
    autoCloseBrackets: true,
    
});

changeMode(syntax_extension);

function changeMode(ext) {
    editor.setOption("mode", ext);
    CodeMirror.autoLoadMode(editor, ext);
}



$("select[name='syntax']").on("change", function () {
    var ext = $(document.getElementById("syntax")).find('option:selected').text();
    changeMode(ext);
});