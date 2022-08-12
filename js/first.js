console.log("开始 hook 猿人学第一题..")


//frida -U --no-pause -f com.yuanrenxue.match2022 -l first.js
setImmediate(function() {
   setTimeout(app1, 5000)
});


function app1() {
    Java.perform(function main() {
        console.log("start insert to app data");

        let utils = Java.use("com.yuanrenxue.match2022.security.Sign");
        utils.sign.overload('[B').implementation = function(bArr){

            console.log("此函数传入的的值为:", byteToString(bArr))
            let result_one = this.sign(bArr)
            console.log("函数执行返回结果为", result_one)
            return result_one;

        }

        // 查看填充的数据
        // utils.padding.overload('[B').implementation = function(bArr){
        //
        //     console.log("此函数传入的的值为1:", byteToString(bArr))
        //     console.log("此函数传入的的值为1:", bArr)
        //     let result_one = this.padding(bArr)
        //     console.log("函数执行返回结果为1", result_one)
        //     return result_one;
        //
        // }

        // 查看常量
        // let other = Java.use("o00OO.OooO0O0")
        // other.OooO0O0.implementation = function(j, strArr){
        //
        //     console.log("此函数传入的的值为1:", j)
        //     console.log("此函数传入的的值为2:", byteToString(strArr))
        //     let result_two = this.OooO0O0(j, strArr)
        //     console.log("函数执行返回结果为", result_two)
        //     return result_two;
        // }
    })
}


// js代码将byte[] 转为 String
function byteToString(arr) {
    if(typeof arr === 'string') {
        return arr;
    }
    let str = '',
        _arr = arr;
    for(let i = 0; i < _arr.length; i++) {
        const one = _arr[i].toString(2),
            v = one.match(/^1+?(?=0)/);
        if(v && one.length === 8) {
            const bytesLength = v[0].length;
            let store = _arr[i].toString(2).slice(7 - bytesLength);
            for(let st = 1; st < bytesLength; st++) {
                store += _arr[st + i].toString(2).slice(2);
            }
            str += String.fromCharCode(parseInt(store, 2));
            i += bytesLength - 1;
        } else {
            str += String.fromCharCode(_arr[i]);
        }
    }
    return str;
}