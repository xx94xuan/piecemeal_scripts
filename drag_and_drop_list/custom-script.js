function dragstartHandler(e) {
    e.dataTransfer.effectedAllowed = 'move';
    e.dataTransfer.setData("text/plain", e.target.id);
}

function dropHandler(e){
    e.preventDefault();

    var data = e.dataTransfer.getData('text');
    e.target.parentNode.insertBefore(document.getElementById(data), e.target);
    // Clear the drag data cache (for all formats/types)
    e.dataTransfer.clearData();
}

function dragoverhandler(e){
    e.preventDefault();
}

