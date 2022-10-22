
function calcActualAS() {
    was = document.getElementById("was").value;
    lasr = document.getElementById("lasr").value;
    pMT = document.getElementById("pMT").value;
    gasr = document.getElementById("gasr").value;
    asMul = document.getElementById("asMul").value;
    attribs = asMul.split(', ');
    console.log(attribs);
    actualAS = parseFloat(was) * (100+parseFloat(lasr)+parseFloat(pMT))/100 * (100+parseFloat(gasr))/100;
    console.log(actualAS);
    for(let i=0; i < attribs.length; i++)
        actualAS = actualAS * parseFloat(attribs[i])
    let html = "";
    html += '<spam> Actual AS is: ' + actualAS + '</spam>';
    $('.outputContainer').append($(html));
}

$(document).ready(function() {
    $('#eqAS').on('click', function() {
        $('.outputContainer').empty();
        calcActualAS();
    });
});