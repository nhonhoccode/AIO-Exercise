import torch
import torch.nn as nn

class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdim=True).values
        x_exp = torch.exp(x - x_max)
        partition = x_exp.sum(0, keepdim=True)
        return x_exp / partition

if __name__ == "__main__":
    data = torch.Tensor([1, 2, 3])
    softmax_stable = SoftmaxStable()
    output = softmax_stable(data)
    print(output)
