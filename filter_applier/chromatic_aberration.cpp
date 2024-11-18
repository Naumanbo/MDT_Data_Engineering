#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>

using namespace std;

// Compile:
// g++ -std=c++11 -o chromatic_aberration chromatic_aberration.cpp `pkg-config --cflags --libs opencv4`

int main() {

    // Load in image
    cout << "Image name (e.g. image.jpg): ";
    string imgname;
    cin >> imgname;
    cv::Mat img = cv::imread(imgname);

    if (img.empty()) {
        cout << "Error opening image" << endl;
        return -1;
    }

    // Split the image into RGB channels
    std::vector<cv::Mat> channels;
    cv::split(img, channels);

    int shift_amount = 0;
    cout << "Input shift amount (int): ";
    cin >> shift_amount;
    cv::Mat shifted_blue, shifted_red, shifted_green;
    cv::warpAffine(channels[0], shifted_blue, cv::Mat::eye(2, 3, CV_32F), img.size(), cv::INTER_LINEAR, cv::BORDER_CONSTANT, cv::Scalar());
    cv::warpAffine(channels[1], shifted_green, cv::Mat::eye(2, 3, CV_32F), img.size(), cv::INTER_LINEAR, cv::BORDER_CONSTANT, cv::Scalar());
    cv::warpAffine(channels[2], shifted_red, cv::Mat::eye(2, 3, CV_32F) + (cv::Mat_<float>(2, 3) << 0, 0, shift_amount, 0, 0, shift_amount), img.size(), cv::INTER_LINEAR, cv::BORDER_CONSTANT, cv::Scalar());
    
    // Merge the shifted channels back
    std::vector<cv::Mat> merged_channels = {shifted_blue, shifted_green, shifted_red};
    cv::Mat output_image;
    cv::merge(merged_channels, output_image);

    // Save the altered image
    cv::imwrite("newimg.jpg", output_image);

   // HERE LIES OLD CODE. //
   // create a copy of the image
   // split both images into separate RGB channels


    // Alter pixel

    // cv::Vec3b newColor(0,255,0);

    // for (int y = 0; y <= 300; ++y) {
    //     for (int x = 0; x <= 300; ++x) {
    //         img.at<cv::Vec3b>(y,x) = newColor;
    //     }
    // }

    // Save image
    // cv::imwrite("newImg.jpg", img);
}