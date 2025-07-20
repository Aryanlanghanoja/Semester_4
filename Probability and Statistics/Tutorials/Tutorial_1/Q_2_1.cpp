#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <sstream>

using namespace std;

class Statistics {
public:
    double Calculate_Median(vector<double>& Data) {
        sort(Data.begin(), Data.end());
        int n = Data.size();
        double Median;
        if (n % 2 == 0) {
            Median = (Data[n / 2 - 1] + Data[n / 2]) / 2.0;
        }
        else {
            Median = Data[n / 2];
        }
        return Median;
    }

    void Calculate_5_Plot_Summary(vector<double>& Data) {
        int size = floor(Data.size() / 2);
        sort(Data.begin(), Data.end());
        double Q1, Q2, Q3;

        Q2 = Calculate_Median(Data);

        if (Data.size() % 2 == 0) {
            vector<double> Lower_Quartile(Data.begin(), Data.begin() + size);
            vector<double> Upper_Quartile(Data.begin() + size, Data.end());
            Q1 = Calculate_Median(Lower_Quartile);
            Q3 = Calculate_Median(Upper_Quartile);
        }
        else {
            vector<double> Lower_Quartile(Data.begin(), Data.begin() + size);
            vector<double> Upper_Quartile(Data.begin() + size + 1, Data.end());
            Q1 = Calculate_Median(Lower_Quartile);
            Q3 = Calculate_Median(Upper_Quartile);
        }

        double Inter_Quartile_Range = Q3 - Q1;
        auto min_element = std::min_element(Data.begin(), Data.end());
        auto max_element = std::max_element(Data.begin(), Data.end());
        double Minimum = *min_element;
        double Maximum = *max_element;
        double Lower_Limit = Q1 - (1.5 * Inter_Quartile_Range);
        double Upper_Limit = Q3 + (1.5 * Inter_Quartile_Range);
        vector<double> Outliers;

        for (int i = 0; i < Data.size(); i++) {
            if (Data[i] < Lower_Limit || Data[i] > Upper_Limit) {
                Outliers.push_back(Data[i]);
            }
        }

        cout << "5 Point Box Plot Summary :- " << endl;
        cout << "Minimum = " << Minimum << endl;
        cout << "Maximum = " << Maximum << endl;
        cout << "Q1 = " << Q1 << endl;
        cout << "Q2 = " << Q2 << endl;
        cout << "Q3 = " << Q3 << endl;
        cout << "Inter Quartile Range = " << Inter_Quartile_Range << endl;
        cout << "Lower Limit = " << Lower_Limit << endl;
        cout << "Upper Limit = " << Upper_Limit << endl;

        if (Outliers.size() > 0) {
            cout << "Outliers = ";
            for (int i = 0; i < Outliers.size(); i++) {
                cout << Outliers[i] << " ";
            }
        }

        else {
            cout << "No Outliers" << endl;
        }
    }
};

int main() {
    string input;

    cout << "Enter A Space Separated Values :-" << endl;
    cin >> input;
    vector<double> numbers;

    istringstream iss(input);
    double num;
    while (iss >> num) {
        numbers.push_back(num);
    }

    return 0;
}
