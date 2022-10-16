
jpeg(file="/Users/fizzausman/desktop/se-02-team-30/static/client/img/covdeathdaily.jpeg")
data <- data.frame(dates = c("2022-01-02", "2022-01-03", "2022-01-04", 
                             "2022-01-05", "2022-01-07", "2022-01-08", 
                             "2022-01-09","2022-01-10", "2022-01-12",
                             "2022-01-13", "2022-01-14", "2022-01-15",
                             "2022-01-17", "2022-01-18", "2022-01-19", 
                             "2022-01-20", "2022-01-21", "2022-01-23", 
                             "2022-01-24","2022-01-25","2022-01-27",
                             "2022-01-28"), 
                  values = c("52", "196", "397", "431", "284", "161", 
                            " 60"," 175"," 331", "261", "232", "144", "143", 
                            " 199", "258", "176", "175", "161", "184"," 182", "179", "172"))

data_new <- data #Duplicate data
data_new$dates <- as.Date(data_new$dates)

plot(data_new$dates, data_new$values,main="daily covid death rates in germany", xlab = "Dates", ylab="Daily Deaths per day",type="b", xaxt="n")

axis(1, data_new$dates,format(data_new$dates, "%d-%m-%Y"))

dev.off()