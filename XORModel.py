import torch
import torch.nn as nn
import torch.nn.functional as F

class XORNetwork(nn.Module):
	def __init__(self):
		super(XORNetwork,self).__init__()
		self.input_layer = nn.Linear(2,2)
		self.hidden_layer = nn.Linear(2,1)

	def forward(self,x):
		x1 = self.input_layer(x)
		x1_ = torch.sigmoid(x1)
		output = self.hidden_layer(x1_)
		return output