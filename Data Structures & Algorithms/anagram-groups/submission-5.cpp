class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        for (auto& s : strs) {
            string key = s;
            sort(key.begin(), key.end());
            groups[key].push_back(s);
        }
        vector<vector<string>> res;
        res.reserve(groups.size());
        for (auto& [key, val] : groups) {
            res.push_back(move(val));
        }
        return res;
    }
};