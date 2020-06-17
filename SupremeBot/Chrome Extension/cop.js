var keyWord, color1, color2;

chrome.runtime.onMessage.addListener(gotMessage);

function gotMessage(message, sender, sendResponse) {
    console.log(message);
    //separates keyword, color1 and color2
    var list = message.split(',');
    keyWord = list[0];
    color1 = list[1];
    color2 = list[2];

    console.log('Copping Items...');
    var keyWordTrue = false;

    //find and click to link
    var div = document.getElementById('container').getElementsByTagName('a');
    //console.log(div[0]);
    for(var i = 0; i < div.length; i++) {
        if (keyWordTrue) {
            if (div[i].innerHTML.indexOf(color1) !== -1 || div[i].innerHTML.indexOf(color2) !== -1) {
                div[i].click();
                break;
            }
        }
        if (div[i].innerHTML.indexOf(keyWord) !== -1) {
            keyWordTrue = true;
        } else {
            keyWordTrue = false;
        }
        sendResponse('Find item done');
    }
}