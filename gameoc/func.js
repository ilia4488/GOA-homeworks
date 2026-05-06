
// 7. .reduce

// მასივი: ['მე', 'მიყვარს', 'JavaScript']

// მიზანი: reduce-ით შეაერთე ეს სიტყვები ერთ გრძელ სტრინგად, მათ შორის ჰქონდეს გამოტოვება (space).

// მოსალოდნელი შედეგი: "მე მიყვარს JavaScript".

// 8. დაასრულეთ საკლასო ვისაც არ დაგისრულებიათ.

// 9. გადახედეთ ჩანაწერს.


// const fruits = ['ვაშლი', 'მსხალი', 'ატამი'];

// fruits.forEach(function(item, index) {
//     console.log(index + ': ' + item);
// });

// const nums = [1, 2, 3, 4, 5, 6];
// nums.forEach(function(num){
    
//         if(num%2==0){
//             console.log("odd")
//         }
//         else{
//             console.log("even")
//         }
    
// });
// const price = [100, 250, 50, 80]
// const newprice=price.map(function(num){
//     return num*0.9
// })
// console.log(newprice)

// const words=['სახლი', 'გზა', 'ავტომობილი', 'ხე']
// const w10=words.some(function(word){
//     return word.length>=10
// })
// console.log(w10)

// const nums=[5, 12, 8, 130, 44];
// const nums2=nums.find(function(num){
//     return num>10
// })
// console.log(nums2)

// const word = ['ვაშლი', 'ბანანი', 'ფორთოხალი', 'ატამი'];
// const orange = word.findIndex(function(wo){
//     return wo === 'ფორთოხალი'
// })
// console.log(orange)

// const arr = ['მე', 'მიყვარს', 'JavaScript']
// const arrr=arr.reduce(function(wo,rd){
//     return wo + ' ' + rd;
// })
// console.log(arrr)


// 5. .some

// მოცემულობა: გაქვს მასივი: [5, 8, -2, 10].

// მიზანი: some-ის გამოყენებით გაარკვიე, არის თუ არა მასივში თუნდაც ერთი უარყოფითი (0-ზე ნაკლები) რიცხვი.

// const nums = [5, 8, -2, 10];
// const numss=nums.some(function(num){
//     return num<0
// })
// console.log(numss)