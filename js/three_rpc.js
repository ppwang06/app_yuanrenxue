// frida rpc调用
function invoke_sign_three(str, j){
    let result = null;
    Java.perform(function main() {
        Java.choose("com.yuanrenxue.match2022.fragment.challenge.ChallengeThreeFragment",{
            onMatch: function (ins) {
                console.log("ins:", ins)
                result = ins.crypto(str, j)
                console.log("result:", result)
            },
            onComplete(){}
        })
    })
    return result
}

rpc.exports = {
    invokeSignThree: invoke_sign_three,
}