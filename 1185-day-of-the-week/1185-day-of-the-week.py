class Solution:
    def dayOfTheWeek(self, d: int, m: int, y: int) -> str:
        e={6:"Sunday",0:"Monday",1: "Tuesday",2: "Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday"}
        import calendar as cl
        a=cl.weekday(y,m,d)
        return e[a]