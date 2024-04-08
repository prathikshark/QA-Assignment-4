from base import TestAssesmentMethods


class Testing():

    def test(self):
        tam = TestAssesmentMethods()
        tam.admin_login()
        tam.redirect_to_report()
        tam.select_employee_status()
        tam.select_checkbox()
        tam.select_plan_year(dates='01/01/2024 to 12/31/2024')
        tam.select_benefit_type(benefit_type='Voluntary Employee Life')
        tam.select_plans(plan_id='s_plans', plan_type='Voluntary Employee Life')
        tam.select_available_plan_fields(plan_id='s_cov_fields', texts=['Created At', 'Change Effective Date'])
        tam.select_available_employee_fields(emp_field_id='s_emp_fields',
                                             texts=["Address 1", "Hire Date",
                                                    "First Name", "Last Name",
                                                    "Gender", "Benefit Salary", "SSN"]
                                             )
        tam.run()
        tam.print_table_data()


Testing().test()
