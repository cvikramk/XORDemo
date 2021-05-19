//
//  ContentView.swift
//  XOR Demo
//
//  Created by Vikram Kamath on 17/05/21.
//

import SwiftUI

struct ContentView: View {
    @State private var show_output = false
    @State private var textbox1 = ""
    @State private var textbox2 = ""
    @State private var inputA = 0
    @State private var inputB = 0
    @State private var modelOutput = 0
    @State private var outputMessage = ""
    @State private var outputState = false
    var body: some View {
        ZStack {
            Color.gray
            VStack {
                HStack {
                    TextField("Input A", text: $textbox1).multilineTextAlignment(.center).foregroundColor(.black).background(Color.white).cornerRadius(100)
                    TextField("Input B", text: $textbox2).multilineTextAlignment(.center).foregroundColor(.black).background(Color.white).cornerRadius(100)//
                }.padding(.leading,50).padding(.trailing,50).padding(.bottom,50)
                Button("XOR", action: {
                    self.show_output = true
                    if (textbox1 == "true" || textbox1 == "True" || textbox1 == "1") {
                        inputA = 1
                    }
                    else if (textbox1 == "false" || textbox1 == "False" || textbox1 == "0") {
                        inputA = 0
                    }
                    else{
                        outputMessage = "Incorrect inputs"
                        self.show_output = false
                    }
                    if (textbox2 == "true" || textbox2 == "True" || textbox2 == "1") {
                        inputB = 1
                    }
                    else if (textbox2 == "false" || textbox2 == "False" || textbox2 == "0") {
                        inputB = 0
                    }
                    else{
                        outputMessage = "Incorrect inputs"
                        self.show_output = false
                    }
                    if (show_output == true){
                        modelOutput = Int(getXOROutput(input_1: inputA, input_2: inputB))
                        if (modelOutput == 0){
                            outputState = false
                        }
                        else if (modelOutput == 1){
                            outputState = true
                        }
                        outputMessage = "Result:  \(outputState)"
                    }
                    
                }).cornerRadius(10).padding()
                .foregroundColor(.white)
                .background(Color.blue)
                HStack {
                    Text("\(outputMessage)").foregroundColor(.black).background(Color.white).frame(width: 300, height: nil).multilineTextAlignment(.center)
                }.padding(.top,50)
            }
            
        }
    }
}

//struct ContentView_Previews: PreviewProvider {
//    static var previews: some View {
//        ContentView()
//    }
//}
