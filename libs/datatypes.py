from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom

IS_A_MEAL_TYPE_RELATIONSHIP = "IS_A_MEAL_TYPE"


class Meal(StructuredNode):
    name = StringProperty(unique_index=True, label="Meal")
    description = StringProperty(unique_index=False)
    meal_types = RelationshipTo("Meal_Type", IS_A_MEAL_TYPE_RELATIONSHIP)


class Meal_Type(StructuredNode):
    name = StringProperty(unique_index=True, label="meal_type")
    description = StringProperty(unique_index=False)
    meals = RelationshipFrom("Meal", IS_A_MEAL_TYPE_RELATIONSHIP)