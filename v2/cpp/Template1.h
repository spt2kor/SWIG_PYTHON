
//=================================================================================
//https://stackoverflow.com/questions/20603707/a-couple-more-swig-warnings
//=================================================================================
/*


When you use templates in SWIG, you can let SWIG know what templates you use so it can generate wrapper code for it. In the case of vector<WString>, you can use:

typedef std::vector<WString> WEditType;
typedef WEditType::iterator  WEditIter;

class WEdit : public WEditType {
%include <std_vector.i>
%template() std::vector<WString>;

*/
//=================================================================================



//=================================================================================



//=================================================================================



