import torch
import torch.nn as nn

class XORNetwork(nn.Module):
	def __init__(self):
		# Initialize the different layers of the network
		super(XORNetwork,self).__init__()
		self.input_layer = nn.Linear(2,2)
		self.hidden_layer = nn.Linear(2,1)

	def forward(self,x):
		# Define forward pass for the model
		x1 = self.input_layer(x)
		x1_ = torch.sigmoid(x1)
		output = self.hidden_layer(x1_)
		return output
