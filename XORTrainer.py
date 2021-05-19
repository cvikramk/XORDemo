import torch
import torch.nn as nn
import numpy as np

from XORModel import XORNetwork

train_data = [[0,0],
			  [1,0],
			  [0,1],
			  [1,1]]

train_labels = [0,1,1,0]

class modelTrainer():
	def __init__(self,epochs=2500,batch_size=4,device="cpu"):
		# Initialize various parameters
		self.device = device
		self.model = XORNetwork().to(self.device)
		self.loss_fn = nn.MSELoss()
		self.optimizer = torch.optim.SGD(self.model.parameters(), lr=0.03,momentum=0.9)
		self.X = torch.Tensor(train_data).to(self.device)
		self.y = torch.Tensor(train_labels).view(-1,1).to(self.device)
		self.train_data_size = len(train_data)
		self.epochs = epochs
		self.batch_size = batch_size
		self.iter_per_epoch = int(self.train_data_size/self.batch_size)

	def getRandomBatch(self):
		# Get a random batch from training data
		randomIds = np.random.randint(0,self.train_data_size,self.batch_size)
		randomX = self.X[randomIds]
		randomY = self.y[randomIds]
		return randomX,randomY
		
	def train(self):
		# Train for given number of epochs
		for i in range(self.epochs):
			for _ in range(self.iter_per_epoch):
				inp, target = self.getRandomBatch() 
				pred = self.model(inp)
				loss = self.loss_fn(pred,target)
				self.optimizer.zero_grad()
				loss.backward()
				self.optimizer.step()
			if i % 500 == 0:
				print("Epoch: {0}, Loss: {1}, ".format(i, loss.data.cpu().numpy()))

	def inference(self,model_input):
		# Run inference on given model input
		self.model.eval()
		with torch.no_grad():
			model_input = torch.Tensor(model_input).to(self.device)
			pred = self.model(model_input)
			return [round(r) for r in pred.flatten().tolist()]

	def saveTracedModel(self,model_path):
		example = torch.Tensor([0,1]).to('cpu')
		traced_script_module = torch.jit.trace(self.model, example)
		traced_script_module.save(model_path)



if __name__ == '__main__':
	XOR_Model = modelTrainer()
	XOR_Model.train()
	XOR_Model.saveTracedModel("./model.pt")
