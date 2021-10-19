# Resource-awaeness-algorithm
Project implemented as a course objective for Real time systems

Fault tolerance has been a hot subject in safety-critical real-time systems due to the vulnerability of computing equipment and program executions to a variety of errors. Furthermore, multicore processors have lately risen to prominence as the primary computational engines for contemporary embedded systems. 

However, there is only a small amount of research on fault-tolerant scheduling of real-time tasks running on multicores with shared resources, where task synchronization caused by resource access contention can severely decrease the task system's schedulability.

We study a utilisation bound and subsequently find an anomaly where the bound may drop as new cores are deployed, with a focus on the partitioned-EDF scheduler using the MSRP (Multiprocessor Stack Resource Policy) protocol and primary/backup recovery mechanism. 

Following the insights gained from the bound analysis, we propose an efficient version of the reliability and synchronisation aware task partitioning algorithm (RSA-TPA) to implement the joint management of task synchronisation and system reliability, where several resource-oriented heuristics are developed to improve both schedulability performance and workload balancing.

When compared to previous schemes that address either reliability management or task synchronisation, comprehensive simulation findings demonstrate that the RSA-TPA methods may achieve greater acceptance ratios (e.g., 60% more) and create more balanced partitions. 

Finally, taking into account the various fault arrival rates, the real implementation in the Linux kernel proves the applicability of RSA-TPA, which has a reduced run-time cost (e.g., 20% less) than alternative mapping methods. 

Refer ppt for more info on the project
