chrome.runtime.onMessage.addListener(gotMessage);

function gotMessage(message, sender, sendResponse) {
    //checkout
    document.getElementsByClassName('button checkout')[0].click();
}