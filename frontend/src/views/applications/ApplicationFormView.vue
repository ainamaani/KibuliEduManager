<template>
  <div>
    <v-container>
      <v-form @submit.prevent="handleApplicationSubmission">
        <h3>Apply for vacancy</h3>
        <v-text-field label="First name" v-model="first_name" :error-messages="getErrors('first_name')" ></v-text-field>
        <v-text-field label="Last name" v-model="last_name" :error-messages="getErrors('last_name')" ></v-text-field>
        <v-text-field label="E-mail" v-model="email" :error-messages="getErrors('email')"></v-text-field>
        <v-radio-group v-model="gender" label="Gender" :error-messages="getErrors('gender')">
          <v-radio label="Male" value="male"></v-radio>
          <v-radio label="Female" value="female"></v-radio>
        </v-radio-group>
        <v-text-field label="Date of birth" v-model="date_of_birth" type="date" :error-messages="getErrors('date_of_birth')" ></v-text-field>
        <v-text-field label="Phone number" v-model="phone_number" :error-messages="getErrors('phone_number')"></v-text-field>
        <v-text-field label="Address" v-model="address" :error-messages="getErrors('address')"></v-text-field>
        <v-select :items="classes" label="Which class are you currently in?" v-model="current_class" :error-messages="getErrors('current_class')" ></v-select>
        <v-text-field label="What is your current school" v-model="school" :error-messages="getErrors('school')"></v-text-field>
        <v-text-field label="What is your current school location" v-model="school_location" :error-messages="getErrors('school_location')"></v-text-field>
        <v-text-field label="What is your current school contact" v-model="school_phone_number" :error-messages="getErrors('school_phone_number')"></v-text-field>
        <v-textarea label="What is your reason for changing schools" v-model="change_reason" :error-messages="getErrors('change_reason')"></v-textarea>
        <v-select :items="classes_to_apply_for" label="Which class are you applying for?" v-model="class_applied_for" :error-messages="getErrors('class_applied_for')"></v-select>
        <v-text-field label="What combination are you interested in doing?" v-model="combination_applied_for" :error-messages="getErrors('combination_applied_for')"></v-text-field>
        <input type="file" @change="handleFileChange($event, 'recommendation_letter')" />
        <input type="file" @change="handleFileChange($event, 'passport')" />
        <input type="file" @change="handleFileChange($event, 'results_document')" />
        <v-text-field label="Guardian name" v-model="guardian_name" :error-messages="getErrors('guardian_name')"></v-text-field>
        <v-text-field label="Guardian E-mail" v-model="guardian_email" :error-messages="getErrors('guardian_email')"></v-text-field>
        <v-text-field label="Guardian contact/phone number" v-model="guardian_phone_number" :error-messages="getErrors('guardian_phone_number')"></v-text-field>
        <v-text-field label="What is your relationship with the above guardian" v-model="relationship_with_guardian" :error-messages="getErrors('relationship_with_guardian')"></v-text-field>
        <v-select label="What is your religion?" :items="religions" v-model="religion" :error-messages="getErrors('religion')"></v-select>
        <v-radio-group v-model="disabled" label="Are you disabled in any way?" :error-messages="getErrors('disabled')">
          <v-radio label="No" value="false"></v-radio>
          <v-radio label="Yes" value="true"></v-radio>
        </v-radio-group>
        <v-textarea v-if="disabled === 'true'" label="What is your disability?" v-model="disabled_description" :error-messages="getErrors('disabled_description')"></v-textarea>
        <v-radio-group v-model="any_chronic_disease_condition" :error-messages="getErrors('any_chronic_disease_condition')" label="Do you have any chronic illness?(e.g athma, stroke, HIV, cancer ,etc)" >
          <v-radio label="No" value="false"></v-radio>
          <v-radio label="Yes" value="true"></v-radio>
        </v-radio-group>
        <v-textarea v-if="any_chronic_disease_condition === 'true'" label="What chronic disease do you have?" v-model="chronic_disease_condition_description" :error-messages="getErrors('chronic_disease_condition_description')"></v-textarea>

        <v-btn variant="elevated" color="primary" type="submit" >Submit application</v-btn>

      </v-form>
    </v-container>
  </div>
</template>

<script>
export default {
    data(){
      return{
        first_name: '',
        last_name: '',
        gender: '',
        email: '',
        date_of_birth : null,
        phone_number: '',
        address: '',
        current_class: '',
        school: '',
        school_location: '',
        school_phone_number: '',
        change_reason: '',
        class_applied_for: '',
        recommendation_letter: null,
        passport: null,
        results_document: null,
        guardian_name: '',
        guardian_phone_number: '',
        guardian_email: '',
        relationship_with_guardian: '',
        religion: '',
        combination_applied_for: '',
        disabled: false,
        disabled_description: '',
        any_chronic_disease_condition: false,
        chronic_disease_condition_description: '',

        classes: ['P7 Vac','F1', 'F2', 'F3', 'F4', 'F4 Vac', 'F5', 'F6'],
        classes_to_apply_for: ['F1', 'F2', 'F3', 'F4', 'F5', 'F6'],
        religions: ['Islam','Christianity'],

        errors: {}

      }
    },
    methods:{
      handleApplicationSubmission (){


        const applicationData = new FormData();
        applicationData.append('first_name', this.first_name)
        applicationData.append('last_name', this.last_name)
        applicationData.append('gender', this.gender)
        applicationData.append('email', this.email)
        applicationData.append('date_of_birth', this.date_of_birth)
        applicationData.append('phone_number', this.phone_number)
        applicationData.append('address', this.address)
        applicationData.append('current_class', this.current_class)
        applicationData.append('school', this.school)
        applicationData.append('school_location', this.school_location)
        applicationData.append('school_phone_number', this.school_phone_number)
        applicationData.append('change_reason', this.change_reason)
        applicationData.append('class_applied_for', this.class_applied_for)
        applicationData.append('recommendation_letter', this.recommendation_letter)
        applicationData.append('passport_photo', this.passport)
        applicationData.append('results_document', this.results_document)
        applicationData.append('guardian_name', this.guardian_name)
        applicationData.append('guardian_email', this.guardian_email)
        applicationData.append('guardian_phone_number', this.guardian_phone_number)
        applicationData.append('relationship_with_guardian', this.relationship_with_guardian)
        applicationData.append('religion', this.religion)
        applicationData.append('combination_applied_for', this.combination_applied_for)
        applicationData.append('disabled', this.disabled)
        applicationData.append('disabled_description', this.disabled_description)
        applicationData.append('any_chronic_disease_condition', this.any_chronic_disease_condition)
        applicationData.append('chronic_disease_condition_description', this.chronic_disease_condition_description)
        
        fetch('http://localhost:8000/api/applications/apply/',{
          method: 'POST',
          
          body: applicationData
        }).then((response)=>{
            if(response.status === 400){
              return response.json();
            }else if(response.status === 201){
            
              console.log("Application submitted successfully")
              this.first_name = '',  this.last_name = '',  this.gender = '',
              this.email = '', this.date_of_birth = null, this.phone_number = '',
              this.address = '', this.current_class = '', this.school = '',
              this.school_location = '', this.school_phone_number = '',
              this.change_reason = '', this.class_applied_for = '',
              this.recommendation_letter = null, this.passport = null,
              this.results_document = null, this.guardian_name = '',
              this.guardian_email = '', this.guardian_phone_number = '',
              this.relationship_with_guardian = '', this.religion = '',
              this.combination_applied_for = '', this.disabled = false,
              this.disabled_description = '', this.any_chronic_disease_condition = false,
              this.chronic_disease_condition_description = ''
            }
        })
        .then((errorData)=>{
          this.errors = errorData;
        })
        .catch((error)=>{
            console.log(error)
        })
      },
      handleFileChange(event, fieldName){
        const file = event.target.files[0]
        this[fieldName] = file;
      },
      getErrors(fieldName) {
        // Check if the field has errors and return an array of error messages
        return this.errors[fieldName] ? this.errors[fieldName] : [];
      },

    }
}
</script>

<style scoped>

</style>