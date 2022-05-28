# Remove Consicutive Characters In A String.
class Partha:
    def solve(self, s):
      seen = s[0]
      ans = s[0]
      for i in s[1:]:
         if i != seen:
            ans += i
            seen = i
      return ans
ob = Partha()
print(ob.solve("PPSSPSPS"))