# PtsV2PaymentsReversalsPost201Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PtsV2PaymentsReversalsPost201ResponseLinks**](PtsV2PaymentsReversalsPost201ResponseLinks.md) |  | [optional] 
**id** | **str** | An unique identification number assigned by CyberSource to identify the submitted request. | [optional] 
**submit_time_utc** | **str** | Time of request in UTC. &#x60;Format: YYYY-MM-DDThh:mm:ssZ&#x60;  Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC.  | [optional] 
**status** | **str** | The status of the submitted transaction. | [optional] 
**reconciliation_id** | **str** | The reconciliation id for the submitted transaction. This value is not returned for all processors.  | [optional] 
**client_reference_information** | [**PtsV2PaymentsPost201ResponseClientReferenceInformation**](PtsV2PaymentsPost201ResponseClientReferenceInformation.md) |  | [optional] 
**reversal_amount_details** | [**PtsV2PaymentsReversalsPost201ResponseReversalAmountDetails**](PtsV2PaymentsReversalsPost201ResponseReversalAmountDetails.md) |  | [optional] 
**processor_information** | [**PtsV2PaymentsReversalsPost201ResponseProcessorInformation**](PtsV2PaymentsReversalsPost201ResponseProcessorInformation.md) |  | [optional] 
**authorization_information** | [**PtsV2PaymentsReversalsPost201ResponseAuthorizationInformation**](PtsV2PaymentsReversalsPost201ResponseAuthorizationInformation.md) |  | [optional] 
**point_of_sale_information** | [**Ptsv2paymentsidreversalsPointOfSaleInformation**](Ptsv2paymentsidreversalsPointOfSaleInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

