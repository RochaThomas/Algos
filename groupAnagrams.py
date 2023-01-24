

# morning algos
# neetcode Group Anagrams

class Solution:
    def groupAnagrams(strs):
        """
        brute force
        check every word against each other, group them, save group, then iterate to next word
        this would probably be a O(n^4)
        for loop to go through strs
        another for loop to go through the rest of the strings
        another loop to go through the first string to get letter
        a last loop to compare all the letters in the rest of the strings
        even space complexity O(n) because you would need to save groups in an array or hashmap

        sort and compare
        hashmap
        sort a word, save as the key, iterate through the strs, sort each str, if it matches key then append it to value array,
        iterate to the next word until, repeat until you go through all the strs
        nlogn to sort, n to go through all the words, and n to compare all the rest of the words
        n^3logn

        faster sort and compare
        hashmap
        iterate through all the words, sort the str (must use "".join(sorted(str)) for strings because there is no sort() method and
        sorted() returns a list of chars instead of a str), if sorted str in hashmap append word to sorted str value array, else new key
        with sorted str and append word to value array, at the end iterate through all the keys appending arrays to a result array
        time complexity probably O(m) for iterating through words and O(nlogn) to sort each word so m*nlogn -> O(mnlogn) 
        and space complexity O(n) for hashmap
        """

        # this solution works!
        sortedStrs = {}

        for str in strs:
            strKey = "".join(sorted(str))
            if strKey in sortedStrs:
                sortedStrs[strKey].append(str)
            else:
                sortedStrs[strKey] = [str]
        
        return sortedStrs.values()

        """
        how can we improve the code and make it more efficient than O(mnlogn)
        we can replace the sorting method by using a count
        reducing the time complexity to O(mn)
        in the hashmap make the key a tuple of the counted chars
        """
        # faster solution

        # res = defaultdict(list)

        # for s in strs:
        #     count = [0] * 26 #a...z

        #     for c in s:
        #         count[ord[c] - ord["a"]] += 1

        #     res[tuple(count)].append(s)
        # return res.values()

    print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))