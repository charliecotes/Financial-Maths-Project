import BarrierOptionPricer

#BarrierOptionPricer.monte_carlo_pricer(100,100,1,0.01828,0.02,0.1,0.05,0.03,"put",0.5,barrier1=80,barrier2=120)

#BarrierOptionPricer.monte_carlo_pricer(100,100,1,0.01828,0.02,0.1,0.05,0.03,"put",0.5,barrier1=80)

#BarrierOptionPricer.monte_carlo_pricer(100,100,1,0.01828,0.02,0.1,0.05,0.03,"put",0.5,barrier2=120)

#BarrierOptionPricer.monte_carlo_pricer(100,100,1,0.01828,0.02,0.1,0.05,0.03,"put",0.5)

#some ideas for additional testing:

#BarrierOptionPricer.monte_carlo_pricer(100,80,1,0.01828,0.02,0.1,0.05,0.03,"call",0.5,barrier1=80,barrier2=120)

#BarrierOptionPricer.monte_carlo_pricer(100,80,1,0.01828,0.04,0.1,0.05,0.03,"call",0.5,barrier1=80,barrier2=120)

#BarrierOptionPricer.monte_carlo_pricer(100,80,1,0.01828,0.04,0.5,0.05,0.03,"call",0.5,barrier1=80,barrier2=120)

#BarrierOptionPricer.monte_carlo_pricer(100,80,1,0.01828,0.04,0.5,0.1,0.03,"call",0.5,barrier1=80,barrier2=120)

BarrierOptionPricer.monte_carlo_pricer(100,80,1,0.01828,0.04,0.5,0.1,0.07,"call",0.5,barrier1=80,barrier2=120)
