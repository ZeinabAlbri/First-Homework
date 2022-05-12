import json
Q1="""The modulation technique used by EDGE are?
A.GMSK and 16QAM
B.GMSK and 8PSK
C.BPSK and 64QAM"""
Q2="""In HSDPA,multiple user share radio resources dynamically using?
A.code multiplexing
B.time multiplexing
C.time and code multiplexinge"""
Q3="""Interleaving is used to obtain?
A.time diversity
B.frequency diversity
C.antenna diversity"""
Q4="""The number of possible modulation and coding scheme in EDGE?
A.4
B.9
C.10"""
Q5="""The guard interval is provided in OFDM?
A.to eliminate PAPR
B.to eliminate ISI
C.both A and B"""
Q6="""Diversity employs the decision making at?
A.transmitter
B.receiver
C.both A and B"""
Q7="""In frequency selective fading the?
A.coherence bandwidth of the channel is less than bandwidth of transmitted channel
B.coherence bandwidth of the channel is more than bandwidth of transmitted channel
C.coherence bandwidth of the channel is equal to bandwidth of transmitted channel"""
Q8="""Types of small scale fading,based on doppler spread are?
A.fast fading
B.flat fading
C. frequency selective fading"""
Q9="""RAKE receiver is?
A.fingers
B.several sub receivers
C.both A and B"""
Q10="""The power delay profile helps in determining?
A.excess delay
B.excess delay spread
C.both A and B"""
Q11="""Flat or frequency nonselective fading is a type of?
A.multipath delay spread small scale fading
B.doppler spread small scale fading
C.both A and B"""
Q12="""Impulse response of a multipath channel is determined by the fact that?
A.mobile radio channel may be modeled as linear filter
B.impulse response is time varying
C.both A and B"""
Q13="""QAM symbols are distinguished by?
A.phase
B.amplitude
C.both A and B"""
Q14="""The peak data rate supported by WCDMA for a stationary user?
A.2.048 Mbps
B.1 Gbps
C.100 Mbps"""
Q15="""CDMA rejects?
A.narrow band interference
B.wide band interference
C.both A and B"""
Q16="""The average uploading speed of 4G LTE network is?
A.5 Gbps
B.500 Mbps
C.300 Mbps"""
Q17="""The radio channel bandwidth of WCDMA is?
A.same as that of GSM
B.5 times that of GSM
C.25 times that of GSM"""
Q18="""In LTE which UE categories support 4x4 MIMO?
A.categories 4 and 5
B.categories 3,4 and 5
C.only category 5"""
Q19="""LTE Rel-10 legacy users access system via?
A.one resource block
B.multiple resource block
C.one component carrier"""
Q20="""The requirement for realtime performance of the UMTS conversational class is?
A.very high
B.high
C.no requirement""" 
d={Q1:"B",Q2:"C",Q3:"A",Q4:"B",Q5:"B",Q6:"B",Q7:"A",Q8:"A",Q9:"C",Q10:"C",Q11:"A",Q12:"C",Q13:"C",Q14:"A",Q15:"A",Q16:"B",Q17:"C",Q18:"C",Q19:"C",Q20:"A"}
z=json.dumps(d)
with open("z.json","w")as f:
    f.write(z)
