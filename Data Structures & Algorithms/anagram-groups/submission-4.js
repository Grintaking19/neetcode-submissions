class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let freqObj = {};
        for (const s of strs){
            let countS = new Array(26).fill(0);
            for (const c of s){
                countS[c.charCodeAt(0) - 'a'.charCodeAt(0)] +=1;
            }
            const key = countS.join(',');
            if(!freqObj[key]){
                freqObj[key] = [];
            }
            freqObj[key].push(s);
        }
        return Object.values(freqObj);
    }
}
