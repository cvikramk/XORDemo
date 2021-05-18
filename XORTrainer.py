import torch
import torch.nn as nn
from torch.utils.mobile_optimizer import optimize_for_mobile
import numpy as np

from XORModel import XORNetwork

train_data = [[0,0],
			  [1,0],
			  [0,1],
			  [1,1]]

train_labels = [0,1,1,0]

class modelTrainer():
	def __init__(self,epochs=1500,batch_size=4):
		self.device = "cuda" if torch.cuda.is_available() else "cpu"
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
		randomIds = np.random.randint(0,self.train_data_size,self.batch_size)
		randomX = self.X[randomIds]
		randomY = self.y[randomIds]
		return randomX,randomY
		
	def train(self):
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
		self.model.eval()
		with torch.no_grad():
			model_input = torch.Tensor(model_input).to(self.device)
			pred = self.model(model_input)
			return [round(r) for r in pred.flatten().tolist()]

	def saveModel(self,model_path):
		torch.save(self.model.state_dict(), model_path)


if __name__ == '__main__':
	XOR_Model = modelTrainer(epochs=2500)
	XOR_Model.train()
	example = [[0,1]]
	traced_script_module = torch.jit.trace(model, example)
	torchscript_model_optimized = optimize_for_mobile(traced_script_module)
	torchscript_model_optimized.save("./xor_model.pt")
	# XOR_Model.saveModel('./xor_model.pt')
	# prediction = XOR_Model.inference([[0,1]])
	# print(prediction)