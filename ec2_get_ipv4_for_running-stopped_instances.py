#!/usr/bin/python

import boto3

client = boto3.client('ec2')
ec2 = boto3.resource('ec2')

#Get the instances in stopped and running states
stopped_instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
running_instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])


# Create lists of running and stopped instances
stopped = []
running = []

for instance in stopped_instances:
    stopped.append(instance.id)

for instance in running_instances:
    running.append(instance.id)

def private_ipv4(list):
    """
    
        This function receive a list of stopped or running instances and
        will print the instance id with its private IPv4 address
    
    """
    for instance in list:
        ip = ec2.Instance(instance).private_ip_address
        print '%s --> %s' %(instance, ip)


# Print the stopped and running instances with their private IPv4 addresses

if len(stopped) == 1:
    print 'The IPv4 address for the stopped instance is:'
    private_ipv4(stopped)
elif len(stopped) > 1:
    print 'The IPv4 addresses for the stopped instances are:'
    private_ipv4(stopped)

if len(running) == 1:
    print 'The IPv4 address for the running instance is:'
    private_ipv4(running)
elif len(running) > 1:
    print 'The IPv4 addresses for the running instances are: '
    private_ipv4(running)




