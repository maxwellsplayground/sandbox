function testPOST(){
    console.log()
    var request = new XMLHttpRequest();
    request.open('POST','/',true);
    request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
    request.send();  

}

$('.interest-list-new').on('input', function() {
    let $this = $(this)
    let $clone = $this.clone()
    let name = $clone.attr('name')
    let n = parseInt(name.split('_')[1]) + 1
    name = 'interest_' + n
      
    $clone.val('')
    $clone.attr('name', name)
    $clone.appendTo($this.parent())
    $this.removeClass('interest-list-new')
    $this.off('input', arguments.callee)
    $clone.on('input', arguments.callee)
})

