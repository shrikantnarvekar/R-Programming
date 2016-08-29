getmode <- function(v)
{
  uniqv=unique(v)
  uniqv[which.max(tabulate(match(v,uniqv)))]
}
d=read.table(header = TRUE, text = "score frequency
              100            10
              200            30
              300            40
              400            60")
d
d2=rep(d$score,d$frequency)
d2
mean(d2)
median(d2)
getmode(d2)
sd(d2) # standard deviation
var(d2) # variance
