import math

class Patient:
    
    def __init__(self, name, weight_kg, height_m):
        
        self.name = name
        self.weight_kg = weight_kg
        self.height_m = height_m
        self.bmi = None

    def calculate_bmi(self):
        
        if self.height_m > 0:
            
            self.bmi = self.weight_kg / (self.height_m ** 2)
            return self.bmi
        else:
            print("Error: Height must be positive to calculate BMI.")
            return None

    def get_bmi_category(self):
       
        if self.bmi is None:
            return "BMI not yet calculated."

        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 25.0:
            return "Normal weight"
        elif 25.0 <= self.bmi < 30.0:
            return "Overweight"
        elif 30.0 <= self.bmi < 35.0:
            return "Obese Class I (Moderate Risk)"
        elif 35.0 <= self.bmi < 40.0:
            return "Obese Class II (High Risk)"
        else:
            return "Obese Class III (Very High Risk)"

    def assess_risk(self):
        
        category = self.get_bmi_category()
        if "Normal" in category:
            return "Risk: Low (Maintain healthy habits)"
        elif "Underweight" in category:
            return "Risk: Potential risks of nutrient deficiency and low immunity. Consultation recommended."
        elif "Overweight" in category:
            return "Risk: Increased risk for cardiovascular disease and type 2 diabetes. Lifestyle changes advised."
        elif "Obese" in category:
            return "Risk: Significant risk for multiple chronic conditions (e.g., heart disease, stroke, diabetes). Urgent consultation recommended."
        else:
            return "Risk assessment pending BMI calculation."

    def display_report(self):
        
       
        print("-" * 50)
        print(f"PATIENT HEALTH METRICS REPORT for: {self.name}")
        print("-" * 50)
        print(f"Weight: {self.weight_kg:.2f} kg")
        print(f"Height: {self.height_m:.2f} m")

        
        if self.bmi is None:
            self.calculate_bmi()

        if self.bmi is not None:
            print(f"Body Mass Index (BMI): {self.bmi:.2f}")
            print(f"BMI Category: {self.get_bmi_category()}")
            print(f"Health Assessment: {self.assess_risk()}")
        else:
            print("Report incomplete due to invalid height/weight data.")
        print("-" * 50)


def main():
    
    
    patient_a = Patient("Alice Johnson", weight_kg=70.5, height_m=1.75)
    patient_a.calculate_bmi()
    patient_a.display_report()

    
    patient_b = Patient("Bob Williams", weight_kg=95.0, height_m=1.78)
    patient_b.calculate_bmi()
    patient_b.display_report()

    
    patient_c = Patient("Charlie Brown", weight_kg=55.0, height_m=1.60)
    
    patient_c.display_report()


    print("\n--- User Input Example ---")
    try:
        name = input("Enter patient name: ")
        weight = float(input("Enter weight in kg (e.g., 75.5): "))
        height = float(input("Enter height in meters (e.g., 1.70): "))

        new_patient = Patient(name, weight, height)
        new_patient.display_report()

    except ValueError:
        print("\nInvalid input. Please enter valid numbers for weight and height.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()