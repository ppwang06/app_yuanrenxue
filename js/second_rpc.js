// frida rpc调用
function invoke_sign(data){
    let result = null;
    Java.perform(function main() {
        Java.choose("com.yuanrenxue.match2022.fragment.challenge.ChallengeTwoFragment",{
            onMatch: function (ins) {
                console.log("ins:", ins)
                result = ins.sign(data)
                console.log("result:", result)
            },
            onComplete(){}
        })
    })
    return result
}

rpc.exports = {
    invokesign: invoke_sign,
}