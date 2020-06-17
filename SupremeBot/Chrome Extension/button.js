var kw, c1, c2, stringEdit;


function buttonClick() {
    console.log("Running SupremeBot...");

    let params = {
        active: true,
        currentWindow: true
    }

    chrome.tabs.query(params, gotTabs)
}

function buttonClick2() {
    let params = {
        active: true,
        currentWindow: true
    }

    chrome.tabs.query(params, gotTabs2)
}

function buttonClick3() {
    let params = {
        active: true,
        currentWindow: true
    }

    chrome.tabs.query(params, gotTabs3)
}

function gotTabs(tabs) {
    kw = document.getElementById("keyword").value;
    c1 = document.getElementById("color1").value;
    c2 = document.getElementById("color2").value;
    stringEdit = kw + "," + c1 + "," + c2;
    console.log(stringEdit);
    chrome.tabs.sendMessage(tabs[0].id, stringEdit);
}

function gotTabs2(tabs) {
    chrome.tabs.sendMessage(tabs[0].id, "add");
}

function gotTabs3(tabs) {
    chrome.tabs.sendMessage(tabs[0].id, "checkout");
}

document.getElementById('cop').addEventListener("click", buttonClick);
document.getElementById('addToCart').addEventListener("click", buttonClick2);
document.getElementById('checkout').addEventListener("click", buttonClick3);