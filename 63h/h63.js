
function robotFactorymodelmobile(model,mobile){
    return{
        model: model,
        mobile: mobile,
        beep(){
            console.log(`Beep Boop! მე ვარ ${this.model}`)
        }
    }
}
robotFactorymodelmobile("prototype","apple").beep()
const personfirstNamesayHellothis = {
    firstname:"Ilia",
    sayname(){
        console.log(this.firstname)
    }
}
personfirstNamesayHellothis.sayname()

const rectanglewidthheightarea = {
    height:100,
    width:100,
    Getter(){
        console.log(this.height*this.width)
    }
}
rectanglewidthheightarea.Getter()