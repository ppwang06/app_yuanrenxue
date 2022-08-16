console.log("开始 hook 猿人学第一题..")


//frida -U --no-pause -f com.yuanrenxue.match2022 -l second.js
setImmediate(function() {
   setTimeout(app2, 5000)
});


function app2() {
    Java.perform(function main() {
        console.log("start insert to app data");

        let utils = Java.use("com.yuanrenxue.match2022.fragment.challenge.ChallengeTwoFragment");
        utils.sign.implementation = function(str){

            console.log("此函数传入的的值为:", str)
            let result_one = this.sign(str)
            console.log("函数执行返回结果为", result_one)
            return result_one;
        }

    })
}