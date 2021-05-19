//
//  ModelLoader.swift
//  XOR Demo
//
//  Created by Vikram Kamath on 18/05/21.
//

import UIKit
import SwiftUI

var module: TorchModule = {
    if let filePath = Bundle.main.path(forResource: "model", ofType: "pt"),
        let module = TorchModule(fileAtPath: filePath) {
        return module
    } else {
        fatalError("Can't find the model file!")
    }
}()

func getXOROutput(input_1: Int,input_2: Int)->Int32 {

    var modelInputList = [Int32(input_1),Int32(input_2)]
    var model_output = module.predict(inputList: &modelInputList) 
    return model_output
}


