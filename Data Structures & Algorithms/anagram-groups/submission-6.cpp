class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        string key;
        for (auto& s : strs) {
            key = s;  // reuses key's buffer when possible
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