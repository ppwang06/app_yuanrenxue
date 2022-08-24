console.log("开始 hook 猿人学第三题..")


//frida -U --no-pause -f com.yuanrenxue.match2022 -l three.js
setImmediate(function() {
   setTimeout(app3, 5000)
});


function app3() {
    Java.perform(function main() {
        console.log("start insert to app data");

        let utils = Java.use("com.yuanrenxue.match2022.fragment.challenge.ChallengeThreeFragment");
        utils.crypto.implementation = function(str, j){

            console.log("此函数传入的的值为:", str, j)
            let result_one = this.crypto(str, j)
            console.log("函数执行返回结果为", result_one)
            return result_one;
        }

    })
}