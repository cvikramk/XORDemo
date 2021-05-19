//
//  TorchModule.h
//  XOR Demo
//
//  Created by Vikram Kamath on 18/05/21.
//

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface TorchModule : NSObject

- (nullable instancetype)initWithFileAtPath:(NSString*)filePath
    NS_SWIFT_NAME(init(fileAtPath:))NS_DESIGNATED_INITIALIZER;
+ (instancetype)new NS_UNAVAILABLE;
- (instancetype)init NS_UNAVAILABLE;
- (int)predictXOROutput:(int*)modelInputs NS_SWIFT_NAME(predict(inputList:));
@end

NS_ASSUME_NONNULL_END
