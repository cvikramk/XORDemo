# XORDemo

A simple iOS app to return output from an XOR Model. The model can be generated and saved from the base folder, and the app code can be found in the `XOR Demo` folder.
## Create and save traced model

```shell
python XORTrainer.py
```
The model will be saved in the base folder and it needs to be moved inside the `XOR Demo` xcode folder.

## Install LibTorch via Cocoapods

The PyTorch C++ library is available in [Cocoapods](https://cocoapods.org/), to integrate it to our project, we can run

```ruby
pod install
```
### Sample screenshot from app

<img src="https://github.com/cvikramk/XORDemo/blob/main/screenshot.png" width="200"/>

