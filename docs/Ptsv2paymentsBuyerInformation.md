# Ptsv2paymentsBuyerInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_customer_id** | **str** | Your identifier for the customer.  For processor-specific information, see the customer_account_id field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  | [optional] 
**date_of_birth** | **str** | Recipient’s date of birth. **Format**: &#x60;YYYYMMDD&#x60;.  This field is a pass-through, which means that CyberSource ensures that the value is eight numeric characters but otherwise does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  | [optional] 
**vat_registration_number** | **str** | Customer’s government-assigned tax identification number.  For processor-specific information, see the purchaser_vat_registration_number field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html)  | [optional] 
**personal_identification** | [**list[Ptsv2paymentsBuyerInformationPersonalIdentification]**](Ptsv2paymentsBuyerInformationPersonalIdentification.md) |  | [optional] 
**hashed_password** | **str** | TODO  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


