data <- read.csv('R/prices_last_three_years.csv')
decompose( data$WTI )
HoltWinters( data$WTI )

library(forecast)

WTI.hwm <- HoltWinters( data$WTI, gamma=FALSE )

WTI.hwf <- forecast.HoltWinters( WTI.hwm, h=4 )

summary( WTI.hwf )

Brent.hwm <- HoltWinters( data$Brent, gamma=FALSE )

Brent.hwf <- forecast.HoltWinters( Brent.hwm, h=4 )

summary( Brent.hwf )

plot.forecast( WTI.hwf )
plot.forecast( Brent.hwf )
