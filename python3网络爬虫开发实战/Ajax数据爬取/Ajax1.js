var xmlhttp;
// 创建一个XMLHttpRequest对象
if(window.XMLHttpRequest){
    //code forIE7+, Firefox, Chrome, Opera, Safari
    xmlhttp=new XMLHttpRequest();
}
else {
    //code for IE6,IE5
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
}

// 调用onreadystatechange属性设置监听
xmlhttp.onreadystatechange=function () {
    if (xmlhttp.readyState==4 && xmlhttp.status==200){
        document.getElementById('myDiv').innerHTML = xmlhttp.responseText;
    }
}

// 调用open()和send()方法向某个链接发送请求
xmlhttp.open('POST', '/ajax/', true)
xmlhttp.send()
